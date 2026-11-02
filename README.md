# Backup & Restore Drill Log

A starter template for running and recording backup and restore
drills: a log sheet to fill in after each drill, a short guide on
how to run one safely, and a worked sample using made-up example
systems. A backup you have never restored is only a hope — a drill
is how you prove, on sample data, that a restore actually works.

## What it is
- `drill-log-template.csv` — one row per drill, with columns for
  the date, the example system, what was backed up, what was
  restored, whether the restore matched, and what was learned.
  The example rows are SAMPLE data only, with invented
  placeholder system names (System A, System B) — they are not
  real systems and the sample results are not real measurements.
- `docs/drill-guide.md` — how to plan a drill, what to check
  before, during, and after a restore, and what to do when a
  drill fails.
- `scripts/drill-summary.py` — a small starter script that reads
  the CSV and summarises drills by result (passed, partial,
  failed) and by system. It reads the CSV only; it touches no
  real backup, runs no restore, and sends nothing anywhere.
- `docs/diagram.png` — a generated Sample / Demo diagram of the
  drill cycle (backup → restore → verify → record). It is an
  illustration, not a screenshot of a real system, and it shows
  no real company system or data.

## How to use it (no code)
1. Copy `drill-log-template.csv` and delete the sample rows.
2. Before a drill, pick ONE non-production sample data set and
   agree what "success" means: the restored files open, the
   record count matches, and the contents match the source.
3. Run the restore into an isolated test location — never over
   live data, and never as a first attempt on a real incident.
4. Fill in one row per drill: date, system, backup type, restore
   target, result, time taken, and lessons learned.
5. Review failed and partial drills first at the next team
   review, and fix the backup job before the next drill — do not
   just re-run the same drill and hope.

## How to use it (with Python)
1. Install Python 3 — no extra packages needed.
2. In a terminal, go to this folder and run:
   `python scripts/drill-summary.py` — summarises every drill
   row by result and by system.
   `python scripts/drill-summary.py --system "System A"` — shows
   only drills for that system.
3. The script only reads the CSV and prints the summary.

## Safety rules (read before any drill)
- Drill on sample or test data only. Never restore over live
  production data, and never use real customer or employee data
  as drill material.
- Never put real passwords, tokens, licence keys, or personal
  data in this log. Record system names generically.
- A passed drill on sample data proves the process works for
  that sample — it is not a guarantee for every real system.
  Drill each important system separately.
- If a drill fails, treat it as a finding, not a failure to
  hide: log it, fix the backup, and re-drill.
- These steps are a starting template, not a policy. Your
  organisation's own backup and data rules always come first.

## Sample data note
All system names, dates, sizes, and results in this repository
are illustrative only. No real system, real data, real company,
or real incident is used anywhere in this repository.

## Note on skills
Python is labelled "Learning" in the author's profile. This script
is an intentionally short, commented starter learning template for
IT support work, and the CSV and guide versions work without it.
No CCTV content is used as experience here, and no performance
numbers are claimed.
