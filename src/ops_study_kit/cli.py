import argparse
from pathlib import Path
from datetime import datetime


def create_report(title: str, output: str) -> None:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)

    content = f"""# {title}

## Date

{datetime.now().strftime("%Y-%m-%d")}

## Goal

Write what you practiced.

## Commands Used

```bash
# example
pwd
ls -la
grep -i "error" app.log
```

## Result

Write the observed result.

## What I Learned

- 

## Next Action

- 
"""
    path.write_text(content, encoding="utf-8")
    print(f"Created report: {path}")


def check_text(file: str, contains: str) -> int:
    path = Path(file)
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8", errors="ignore")
    if contains in text:
        print(f"PASS: found '{contains}' in {path}")
        return 0

    print(f"FAIL: '{contains}' not found in {path}")
    return 1


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="ops-study-kit",
        description="DevOps/SRE beginner lab helper and report generator",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    report = sub.add_parser("new-report", help="Create a Markdown study report")
    report.add_argument("--title", required=True)
    report.add_argument("--output", required=True)

    check = sub.add_parser("check-text", help="Check whether a file contains text")
    check.add_argument("--file", required=True)
    check.add_argument("--contains", required=True)

    args = parser.parse_args()

    if args.command == "new-report":
        create_report(args.title, args.output)
        return

    if args.command == "check-text":
        raise SystemExit(check_text(args.file, args.contains))


if __name__ == "__main__":
    main()
