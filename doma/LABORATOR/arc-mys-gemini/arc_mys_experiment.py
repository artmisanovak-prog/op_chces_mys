import argparse, json, os, random, re, time
from pathlib import Path
from google import genai

BASELINE = """Solve the ARC task from the training input/output pairs. Return ONLY JSON with exactly two predictions: {"attempt_1":[[...]],"attempt_2":[[...]]}. Each grid is a rectangular array of integers 0..9. No markdown."""
MYS = """Solve the ARC task using this procedure: (1) record observed facts without interpreting them prematurely; (2) propose a small set of plausible transformation hypotheses; (3) test each against EVERY training pair and reject contradictions; (4) keep multiple hypotheses if evidence does not decide; (5) return the two best distinct test-grid predictions. Do not force a single explanation before checking the examples. Return ONLY JSON with exactly two predictions: {"attempt_1":[[...]],"attempt_2":[[...]]}. Each grid is a rectangular array of integers 0..9. No markdown."""

def parse(text):
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", (text or "").strip(), flags=re.I)
    try: return json.loads(text)
    except Exception:
        m = re.search(r"\{.*\}", text, re.S)
        if not m: raise ValueError("Model did not return JSON")
        return json.loads(m.group())

def valid(g):
    return isinstance(g,list) and len(g)>0 and all(isinstance(r,list) and len(r)>0 for r in g) and len({len(r) for r in g})==1 and all(type(v)==int and 0<=v<=9 for r in g for v in r)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--data",required=True,help="ARC training.json")
    p.add_argument("--out",default="arc_mys_results")
    p.add_argument("--n",type=int,default=10)
    p.add_argument("--seed",type=int,default=20261011)
    p.add_argument("--model",default="gemini-2.5-flash")
    p.add_argument("--pause",type=float,default=1.0)
    p.add_argument("--resume",action="store_true")
    a=p.parse_args()
    key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not key: raise SystemExit("Set GEMINI_API_KEY securely; do not paste it into the script.")
    client=genai.Client(api_key=key)
    tasks=json.loads(Path(a.data).read_text(encoding="utf-8"))
    eligible=[(tid,t) for tid,t in tasks.items() if len(t.get("test",[]))==1 and "output" in t["test"][0]]
    rng=random.Random(a.seed); sample=rng.sample(eligible,min(a.n,len(eligible)))
    out=Path(a.out); out.mkdir(parents=True,exist_ok=True); path=out/"results.jsonl"
    done=set()
    if a.resume and path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                x=json.loads(line); done.add((x["task_id"],x["variant"]))
            except Exception: pass
    with path.open("a",encoding="utf-8") as f:
        for i,(tid,t) in enumerate(sample,1):
            payload={"training":t["train"],"test_inputs":[x["input"] for x in t["test"]]}
            for variant,inst in (("baseline",BASELINE),("mys",MYS)):
                if (tid,variant) in done: continue
                row={"task_id":tid,"variant":variant,"model":a.model}
                try:
                    r=client.models.generate_content(model=a.model,contents=inst+"\n\nTASK JSON:\n"+json.dumps(payload,separators=(",",":")),config={"temperature":0})
                    obj=parse(r.text)
                    preds=[obj.get("attempt_1"),obj.get("attempt_2")]
                    preds=[g for g in preds if valid(g)]
                    if not preds: raise ValueError("No valid prediction grids")
                    truth=t["test"][0]["output"]
                    row.update(predictions=preds,truth=truth,correct=int(any(g==truth for g in preds)),raw_response=r.text)
                except Exception as e: row.update(error=repr(e),correct=0)
                f.write(json.dumps(row,ensure_ascii=False)+"\n"); f.flush()
                print(f"[{i}/{len(sample)}] {tid} {variant}: {row['correct']}" + (f" ERROR {row['error']}" if "error" in row else ""))
                time.sleep(a.pause)
    rows=[json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
    ids={tid for tid,_ in sample}; rows=[r for r in rows if r.get("task_id") in ids]
    summary={}
    for v in ("baseline","mys"):
        rr=[r for r in rows if r["variant"]==v]
        summary[v]={"tasks":len(rr),"correct":sum(int(r.get("correct",0)) for r in rr),"accuracy":sum(int(r.get("correct",0)) for r in rr)/len(rr) if rr else None,"errors":sum("error" in r for r in rr)}
    (out/"summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print(json.dumps(summary,indent=2))
if __name__=="__main__": main()
