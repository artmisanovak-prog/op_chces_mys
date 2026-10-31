#!/usr/bin/env python3
"""Paired ARC-AGI-2 run: same local Transformers model, baseline vs MOUSE context."""
import argparse, hashlib, json, random, re, time
from pathlib import Path
from typing import Any
import torch
from transformers import AutoProcessor, AutoModelForImageTextToText

SYSTEM = ("You solve ARC-AGI-2 grid transformations. Infer the rule from training "
          "examples and apply it to each test input. Return only JSON: "
          '{"predictions":[[[integer,...],...], ...]}. No markdown.")

def parse_predictions(text):
    candidates=[text.strip()]
    m=re.search(r"\{.*\}",text,re.S)
    if m: candidates.append(m.group(0))
    for s in candidates:
        try:
            obj=json.loads(s); value=obj.get("predictions") if isinstance(obj,dict) else obj
            if isinstance(value,list) and all(isinstance(g,list) and all(isinstance(r,list) for r in g) for g in value):
                return value
        except Exception: pass
    return None

def make_prompt(task, context=None):
    parts=[]
    if context:
        parts.append("MOUSE WORKING CONTEXT. Treat as hypotheses about relations, not ARC answers. Use only if supported by ARC examples.\n"+context)
    parts.append("ARC training examples:")
    for i,pair in enumerate(task.get("train",[]),1):
        parts.append("Example "+str(i)+"\nINPUT:\n"+json.dumps(pair["input"])+"\nOUTPUT:\n"+json.dumps(pair["output"]))
    parts.append("ARC test inputs:")
    for i,pair in enumerate(task.get("test",[]),1):
        parts.append("Test "+str(i)+"\nINPUT:\n"+json.dumps(pair["input"]))
    parts.append("Return "+str(len(task.get("test",[])))+" predictions in JSON under key predictions.")
    return "\n\n".join(parts)

def generate(model, processor, prompt, max_tokens):
    text=SYSTEM+"\n\n"+prompt
    messages=[{"role":"user","content":[{"type":"text","text":text}]}]
    try:
        inputs=processor.apply_chat_template(messages,tokenize=True,add_generation_prompt=True,return_tensors="pt",return_dict=True)
    except Exception:
        inputs=processor(text=text,return_tensors="pt")
    inputs={k:(v.to(model.device) if hasattr(v,"to") else v) for k,v in inputs.items()}
    start=time.time()
    with torch.inference_mode(): output=model.generate(**inputs,max_new_tokens=max_tokens,do_sample=False)
    seconds=time.time()-start
    if "input_ids" in inputs: output=output[:,inputs["input_ids"].shape[-1]:]
    return processor.batch_decode(output,skip_special_tokens=True)[0],seconds

def run_branch(model,processor,folder,paths,outfile,branch,context,max_tokens):
    summary={"branch":branch,"tasks_run":0,"tasks_scored":0,"exact_matches":0}
    outfile.parent.mkdir(parents=True,exist_ok=True)
    with outfile.open("w",encoding="utf-8") as out:
        for n,path in enumerate(paths,1):
            task=json.loads(path.read_text(encoding="utf-8"))
            prompt=make_prompt(task,context)
            raw,seconds=generate(model,processor,prompt,max_tokens)
            pred=parse_predictions(raw)
            expected=[p.get("output") for p in task.get("test",[])]
            scored=bool(expected) and all(x is not None for x in expected)
            correct=bool(scored and pred==expected)
            row={"branch":branch,"task_id":path.stem,"prompt":prompt,"raw_response":raw,
                 "parsed_predictions":pred,"expected_outputs":expected if scored else None,
                 "scored":scored,"exact_match":correct if scored else None,"seconds":round(seconds,3)}
            out.write(json.dumps(row,ensure_ascii=False)+"\n")
            summary["tasks_run"]+=1
            if scored:
                summary["tasks_scored"]+=1; summary["exact_matches"]+=int(correct)
            print("["+branch+"] "+str(n)+"/"+str(len(paths))+" "+path.stem+" "+("CORRECT" if correct else "WRONG" if scored else "UNSCORABLE"))
    summary["accuracy"]=summary["exact_matches"]/summary["tasks_scored"] if summary["tasks_scored"] else None
    summary["trace_file"]=str(outfile)
    return summary

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--data",default="data/arc-agi-2/source/data/training")
    ap.add_argument("--split",choices=["training","evaluation"],default="training")
    ap.add_argument("--model",default="Qwen/Qwen2.5-VL-3B-Instruct")
    ap.add_argument("--mouse-context",default="")
    ap.add_argument("--limit",type=int,default=10)
    ap.add_argument("--seed",type=int,default=17)
    ap.add_argument("--max-new-tokens",type=int,default=1200)
    ap.add_argument("--out",default="experiments/runs")
    args=ap.parse_args()
    folder=Path(args.data)
    if args.split=="evaluation" and "evaluation" not in str(folder).lower():
        raise SystemExit("Safety stop: evaluation split requires an evaluation folder.")
    available=sorted(folder.glob("*.json"))
    if not available: raise SystemExit("No task JSON files. Run prepare_arc_data.py first.")
    rng=random.Random(args.seed)
    paths=sorted(rng.sample(available,min(max(1,args.limit),len(available))),key=lambda p:p.name)
    context_path=Path(args.mouse_context) if args.mouse_context else None
    context=context_path.read_text(encoding="utf-8") if context_path else None
    if context is not None and not context.strip(): raise SystemExit("MOUSE context file is empty.")
    processor=AutoProcessor.from_pretrained(args.model,trust_remote_code=True)
    model=AutoModelForImageTextToText.from_pretrained(args.model,torch_dtype="auto",device_map="auto",trust_remote_code=True)
    model.eval()
    run_id=time.strftime("%Y%m%d-%H%M%S"); outdir=Path(args.out)/run_id; outdir.mkdir(parents=True,exist_ok=True)
    config={"run_id":run_id,"model":args.model,"split":args.split,"seed":args.seed,
            "task_ids":[p.stem for p in paths],"mouse_context_file":str(context_path) if context_path else None,
            "mouse_context_sha256":hashlib.sha256(context_path.read_bytes()).hexdigest() if context_path else None,
            "max_new_tokens":args.max_new_tokens}
    (outdir/"config.json").write_text(json.dumps(config,indent=2,ensure_ascii=False),encoding="utf-8")
    baseline=run_branch(model,processor,folder,paths,outdir/"baseline.jsonl","baseline",None,args.max_new_tokens)
    mouse=run_branch(model,processor,folder,paths,outdir/"mouse.jsonl","mouse",context,args.max_new_tokens)
    result={"config":config,"baseline":baseline,"mouse":mouse}
    (outdir/"summary.json").write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=="__main__": main()
