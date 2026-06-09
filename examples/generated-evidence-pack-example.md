# Linux grep/find practice

> Example only. This file shows what a generated evidence pack can look like.

## Area

linux

## Date

2026-06-09

## Goal

Practice the difference between finding files and searching inside files.

## Environment

- OS: WSL Ubuntu
- Tool version: ops-study-kit 0.3.0
- Notes: sample log practice only

## Commands Run

```bash
find examples -name "*.log"
grep -i "error" examples/linux-grep-find-sample.log
```

## Expected Result

Find log files and search for error lines inside the sample log.

## Observed Result

The sample log contained error lines that matched the search pattern.

## Validation

The command output was checked against the expected sample log contents.

## Mistake or Confusion

At first, it was easy to confuse `find` and `grep`.

## What I Changed

Separated file-path search from content search.

## What I Learned

`find` searches file paths and metadata. `grep` searches inside file contents.

## Portfolio Summary

I practiced basic Linux log investigation and documented the difference between file discovery and content search.

## Next Practice

Practice combining `find`, `grep`, pipes, and command substitution.
