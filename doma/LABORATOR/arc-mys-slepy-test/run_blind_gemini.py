#!/usr/bin/env python3
"""Run a model on blind ARC tasks. This script never opens the answer key."""
import argparse, json, os, re, time
from pathlib import Path
from google import genai

BASELINE = """Solve this ARC task from the training input/output examples. Infer the transformation and apply it to the test input. Return only JSON with keys hypotheses, observations, attempt_1, attempt_2. Grids must be rectangular arrays of integers 0..9. No markdown."""
MYS = """Treat each training pair as observations, not as an already explained rule. Record anomalies, asymmetries, exceptions, and repetitions. Propose multiple plausible transformation hypotheses. Test each against EVERY training pair and reject contradictions. Do not dismiss an anomaly as noise without evidence. Prefer the simplest rule that explains all examples without unsupported assumptions. Apply the surviving rule to the test input. Return only JSON with keys hypotheses, observations, attempt_1, attempt_2. Grids must be rectangular arrays of integers 0..9. No markdown."""

def parse_json(s):
    s=(s or "").strip()
    s=re.sub(r"^```(?:json)?\s*","",s,flags=re.I)
    s=re.sub(r"\s*```$","",s)
    try: return json.loads(s)
    except json.JSONDecodeError:
        m=re.search(r"\{.*\}",s,re.S)
        if not m: raise ValueError("Response was not JSON")
        return json.loads(m.group(0))

def valid_grid(g):
    return (isinstance(g,list) and bool(g) and all(isinstance(r,list) and bool(r) for r in g)
        and len({len(r) for r in g})==1 and all(type(v) is int and 0<=v<=9 for r in g for v in r))

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--blind",required=True,help="blind_tasks.json; must not contain outputs")
    p.add_argument("--out",default="predictions")
    p.add_argument("--model",default="gemini-2.5-flash")
    p.add_argument("--variant",choices=["mys","baseline"],default="mys")
    p.add_argument("--pause",type=float,default=1.0)
    p.add_argument("--resume",action="store_true")
    a=p.parse_args()
    key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not key: raise SystemExit("Set GEMINI_API_KEY securely via environment or Kaggle Secrets.")
    client=genai.Client(api_key=key)
    tasks=json.loads(Path(a.blind).read_text(encoding="utf-8"))
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    path=out/f"{a.variant}_predictions.jsonl";done=set()
    if a.resume and path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            try: done.add(json.loads(line)["task_id"])
            except Exception: pass
    instruction=MYS if a.variant=="mys" else BASELINE
    with path.open("a",encoding="utf-8") as f:
        for i,(tid,task) in enumerate(tasks.items(),1):
            if tid in done: continue
            payload={"training":task["train"],"test_inputs":[x["input"] for x in task["test"]]}
            row={"task_id":tid,"variant":a.variant,"model":a.model}
            try:
                resp=client.models.generate_content(model=a.model,
                    contents=instruction+"\n\nTASK JSON:\n"+json.dumps(payload,separators=(",",":")),
                    config={"temperature":0})
                obj=parse_json(resp.text);preds=[]
                for k in ("attempt_1","attempt_2"):
                    g=obj.get(k)
                    if valid_grid(g) and g not in preds: preds.append(g)
                row.update(predictions=preds,hypotheses=obj.get("hypotheses",[]),
                    observations=obj.get("observations",[]),raw_response=resp.text)
                if not preds: row["error"]="NO_VALID_GRID"
            except Exception as e: row.update(predictions=[],error=repr(e))
            f.write(json.dumps(row,ensure_ascii=False)+"\n");f.flush()
            print(f"[{i}/{len(tasks)}] {tid}: {len(row.get('predictions',[]))} predictions")
            time.sleep(max(0,a.pause))
    print(f"Predictions saved to {path}. Answer key was not loaded.")
if __name__=="__main__": main()
