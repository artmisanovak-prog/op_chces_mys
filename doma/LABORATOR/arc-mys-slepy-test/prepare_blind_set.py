#!/usr/bin/env python3
"""Create a blind ARC evaluation set and a separate private answer key."""
import argparse
import json
import random
from pathlib import Path

def is_grid(grid):
    return (isinstance(grid, list) and bool(grid)
        and all(isinstance(row, list) and bool(row) for row in grid)
        and len({len(row) for row in grid}) == 1
        and all(type(cell) is int and 0 <= cell <= 9 for row in grid for cell in row))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="ARC JSON object: task_id -> train/test")
    parser.add_argument("--out", default="blind_eval")
    parser.add_argument("--n", type=int, default=120)
    parser.add_argument("--seed", type=int, default=20261011)
    args = parser.parse_args()
    if args.n < 1: parser.error("--n must be at least 1")
    source = json.loads(Path(args.data).read_text(encoding="utf-8"))
    if not isinstance(source, dict):
        raise SystemExit("Input must be a JSON object mapping task IDs to ARC tasks.")
    eligible, rejected = [], 0
    for task_id, task in source.items():
        if not isinstance(task, dict):
            rejected += 1
            continue
        tests, train = task.get("test", []), task.get("train", [])
        if (isinstance(train, list) and train and isinstance(tests, list) and len(tests) == 1
            and isinstance(tests[0], dict) and is_grid(tests[0].get("input"))
            and is_grid(tests[0].get("output"))
            and all(is_grid(pair.get("input")) and is_grid(pair.get("output")) for pair in train if isinstance(pair, dict))
            and all(isinstance(pair, dict) for pair in train)):
            eligible.append((task_id, task))
        else: rejected += 1
    if len(eligible) < args.n:
        raise SystemExit(f"Only {len(eligible)} eligible tasks; requested {args.n}. Rejected: {rejected}.")
    chosen = random.Random(args.seed).sample(eligible, args.n)
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    blind, answer_key = {}, {}
    for task_id, task in chosen:
        blind[task_id] = {"train": task["train"], "test": [{"input": task["test"][0]["input"]}]}
        answer_key[task_id] = {"output": task["test"][0]["output"]}
    (out / "blind_tasks.json").write_text(json.dumps(blind, ensure_ascii=False), encoding="utf-8")
    (out / "answer_key.json").write_text(json.dumps(answer_key, ensure_ascii=False), encoding="utf-8")
    (out / "task_ids.txt").write_text("\n".join(blind) + "\n", encoding="utf-8")
    print(f"Created {len(blind)} tasks; rejected {rejected}; seed={args.seed}.")
    print(f"Model input: {out / 'blind_tasks.json'}")
    print(f"Keep private until inference is complete: {out / 'answer_key.json'}")

if __name__ == "__main__": main()
