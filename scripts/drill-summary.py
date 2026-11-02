#!/usr/bin/env python3
"""Starter learning template: summarise a backup/restore drill log.

Reads drill-log-template.csv (sample data only) and prints how many
drills passed, were partial, or failed, overall and per system.
It touches no real backup, runs no restore, and sends nothing
anywhere. Usage:
    python scripts/drill-summary.py
    python scripts/drill-summary.py --system "System A"
"""
import argparse
import csv
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(HERE, "drill-log-template.csv")


def main():
    parser = argparse.ArgumentParser(description="Summarise drill log rows.")
    parser.add_argument("--system", default=None, help="Show only this system")
    args = parser.parse_args()

    if not os.path.exists(CSV_PATH):
        print(f"CSV not found: {CSV_PATH}", file=sys.stderr)
        return 1

    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if args.system and row["system"] != args.system:
                continue
            rows.append(row)

    if not rows:
        print("No drill rows matched.")
        return 0

    print(f"Drills: {len(rows)}")
    print("By result:")
    for result, count in Counter(r["result"] for r in rows).most_common():
        print(f"  {result}: {count}")
    print("By system:")
    for system, count in Counter(r["system"] for r in rows).most_common():
        print(f"  {system}: {count}")
    times = [int(r["time_minutes"]) for r in rows if r["time_minutes"].isdigit()]
    if times:
        print(f"Average restore time: {sum(times) / len(times):.1f} minutes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
