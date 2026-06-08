import argparse
from pathlib import Path
from datetime import datetime


RESOURCE_ENTRIES = (
    ("Korean beginner quickstart", "docs/ko/quickstart.md"),
    ("Linux grep/find lab", "examples/linux-grep-find-lab.md"),
    ("Networking ping vs curl lab", "examples/networking-ping-vs-curl-lab.md"),
    ("AWS S3 beginner lab template", "templates/aws-s3-beginner-lab.md"),
    ("AWS S3 evidence example", "examples/aws-s3-evidence-example.md"),
    ("Korean study report template", "templates/study-report-ko.md"),
    ("Japanese study report template", "templates/study-report-ja.md"),
)


def get_resource_list() -> str:
    lines = ["Available resources:"]
    lines.extend(f"- {label}: {path}" for label, path in RESOURCE_ENTRIES)
    return "\n".join(lines)


def list_resources() -> None:
    print(get_resource_list())


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

    sub.add_parser("list-resources", help="Show available docs, labs, and templates")

    args = parser.parse_args()

    if args.command == "new-report":
        create_report(args.title, args.output)
        return

    if args.command == "check-text":
        raise SystemExit(check_text(args.file, args.contains))

    if args.command == "list-resources":
        list_resources()
        return


if __name__ == "__main__":
    main()
