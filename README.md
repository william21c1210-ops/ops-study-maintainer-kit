# Ops Study Maintainer Kit

A beginner-friendly open-source toolkit for practicing DevOps/SRE fundamentals through small, reproducible Linux and networking labs.

## Why this project exists

Many beginner learners study Linux, networking, and cloud concepts separately, but struggle to prove what they actually did. This project turns small practice tasks into a repeatable workflow:

1. run a small lab,
2. collect command output,
3. validate the result,
4. generate a Markdown learning report,
5. keep a public trail of issues, fixes, and releases.

The goal is to help new learners build operational evidence, not just notes.

## Core features

- Python CLI for creating and validating simple ops-learning labs
- Markdown report generation from lab results
- Templates for GitHub issues, pull requests, and release notes
- Beginner-friendly examples for Linux and networking study
- CI workflow for tests and basic quality checks

## Example use cases

- Check whether a learner understands `grep`, `find`, pipes, and redirection
- Generate a report after a Linux command practice session
- Convert study logs into portfolio-ready evidence
- Maintain a small open-source learning repository with issues, releases, and tests

## Installation

```bash
git clone https://github.com/william21c1210-ops/ops-study-maintainer-kit.git
cd ops-study-maintainer-kit
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

```bash
ops-study-kit new-report --title "Linux grep and pipe practice" --output examples/report.md
ops-study-kit check-text --file examples/sample.log --contains ERROR
```

## Roadmap

- [ ] Add Linux command validation presets
- [ ] Add networking mini-labs: HTTP status, DNS, ping vs curl
- [ ] Add AWS beginner labs: S3, IAM, EC2 basics
- [ ] Add Korean and Japanese learning report templates
- [ ] Add issue triage helpers for beginner contributors

## Maintainer workflow

This repository is maintained as a learning-oriented OSS project. Maintenance work includes:

- issue triage
- documentation updates
- test improvements
- release notes
- beginner contribution review
- automation for report generation and validation

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. See [LICENSE](LICENSE).
