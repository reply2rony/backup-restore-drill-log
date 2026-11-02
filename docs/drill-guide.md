# Backup & Restore Drill Guide

A short starter guide. Adapt it to your organisation's own rules —
this guide does not replace them.

## 1. Before the drill
- Pick one sample data set (test files you can afford to lose).
- Write down what success means before you start: files open,
  record counts match, contents match the source.
- Confirm where the restore will go: an isolated test folder,
  never the live location.
- Note the backup to test: its date, type (full, incremental,
  or other), and where it is stored — generically, not with
  real server names or credentials.

## 2. During the drill
- Restore the sample backup into the isolated test location.
- Time the restore from start to finish.
- Check the restored files: do they open, do counts match,
  does a spot-check of contents match the source?
- If anything is unclear, stop and note it — a drill that
  "mostly worked" is a partial result, not a pass.

## 3. After the drill
- Log one row: date, system (generic name), backup type,
  restore target, result (passed / partial / failed),
  time taken, and lessons learned.
- For a partial or failed drill: record what broke, fix the
  backup job, and schedule a re-drill. Do not delete the
  failed row — the history is the point.
- Review the log regularly: systems with no recent drill are
  the ones to drill next.

## 4. A simple drill schedule (starter suggestion)
- Drill each important system at least once per quarter.
- Drill again after any backup job change, storage change,
  or failed drill.
- Keep the log: a year of drill rows is worth more than a
  single "we tested it once" claim.

## What this guide is not
- It is not a disaster-recovery plan and not a backup product.
- It does not test real production restores — drills use
  sample data in an isolated location.
- All examples here use invented placeholder names only.
