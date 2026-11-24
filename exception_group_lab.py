#!/usr/bin/env python3
"""Demonstrate how except* splits an ExceptionGroup by type."""
from __future__ import annotations
import argparse, json
from typing import Any

def run_demo() -> list[dict[str, Any]]:
    handled: list[dict[str, Any]] = []
    try:
        raise ExceptionGroup("three independent operations failed", [
            ValueError("invalid age"), TypeError("expected a string"),
            OSError("file unavailable"), ValueError("invalid score"),
        ])
    except* ValueError as group:
        handled.append({"handler":"ValueError","count":len(group.exceptions),"messages":[str(e) for e in group.exceptions]})
    except* TypeError as group:
        handled.append({"handler":"TypeError","count":len(group.exceptions),"messages":[str(e) for e in group.exceptions]})
    except* OSError as group:
        handled.append({"handler":"OSError","count":len(group.exceptions),"messages":[str(e) for e in group.exceptions]})
    return handled

def main() -> None:
    parser=argparse.ArgumentParser(description="Explore Python ExceptionGroup and except*.")
    parser.add_argument("--json",action="store_true",help="print JSON output")
    args=parser.parse_args()
    result=run_demo()
    if args.json:
        print(json.dumps(result,indent=2)); return
    print("ExceptionGroup was split into matching subgroups:")
    for row in result:
        print(f'- {row["handler"]}: {row["count"]} exception(s)')
        for message in row["messages"]: print(f"    • {message}")

if __name__=="__main__": main()
