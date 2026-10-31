#!/usr/bin/env python3
"""Offline ARC evaluator. Run only after inference is complete."""
import argparse, json
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--answers",required=True,help="Private answer_key.json")
    p.add_argument("--predictions",required=True,help="*_predictions.jsonl")
    p.add_argument("--out",default="evaluation.json")
    a=p.parse_args()
    key=json.loads(Path(a.answers).read_text(encoding="utf-8"))
    rows=[json.loads(x) for x in Path(a.predictions).read_text(encoding="utf-8").splitlines() if x.strip()]
    by_id={}
    for row in rows:
        tid=row.get("task_id")
        if tid in by_id: raise SystemExit(f"Duplicate prediction row for task {tid}; resolve before scoring.")
        by_id[tid]=row
    unknown=set(by_id)-set(key)
    if unknown: raise SystemExit(f"Predictions contain task IDs absent from answer key: {sorted(unknown)[:10]}")
    scored=[]
    for tid, answer in key.items():
        r=by_id.get(tid,{})
        truth=answer["output"]; preds=r.get("predictions",[])
        scored.append({"task_id":tid,"variant":r.get("variant"),"correct_top1":bool(preds and preds[0]==truth),
            "correct_top2":any(x==truth for x in preds[:2]),"n_predictions":len(preds),
            "hypotheses":r.get("hypotheses",[]),"observations":r.get("observations",[]),
            "error":r.get("error", "MISSING_PREDICTION_ROW" if tid not in by_id else None)})
    variants=sorted({r.get("variant","unknown") for r in rows})
    if len(variants)>1: raise SystemExit("One prediction file must contain only one variant; evaluate baseline and Myš separately.")
    variant=variants[0] if variants else "unknown"; n=len(scored)
    summary={variant:{"tasks_in_answer_key":n,"prediction_rows":len(rows),
        "top1_correct":sum(x["correct_top1"] for x in scored),"top1_accuracy":sum(x["correct_top1"] for x in scored)/n if n else None,
        "top2_correct":sum(x["correct_top2"] for x in scored),"top2_accuracy":sum(x["correct_top2"] for x in scored)/n if n else None,
        "missing_prediction_rows":sum(x["error"]=="MISSING_PREDICTION_ROW" for x in scored),
        "api_or_parse_errors":sum(bool(x["error"]) and x["error"]!="MISSING_PREDICTION_ROW" for x in scored)}}
    result={"summary":summary,"per_task":scored}
    Path(a.out).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    print(f"Detailed evaluation saved to {a.out}")
if __name__=="__main__": main()
