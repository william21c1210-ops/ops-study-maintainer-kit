# Ops Study Maintainer Kit

A beginner-friendly open-source toolkit for practicing DevOps/SRE fundamentals through small, reproducible Linux and networking labs.

## Project status

This is an early public OSS project with an exercised maintainer workflow: CI, tests, issue templates, a public roadmap, milestones, release notes, pull requests, and closed issues.

The project is building durable OSS foundations before expanding CLI features, validation helpers, and contributor-facing documentation.

Operational links:

- [Issues](https://github.com/william21c1210-ops/ops-study-maintainer-kit/issues)
- [Milestone v0.2.0](https://github.com/william21c1210-ops/ops-study-maintainer-kit/milestone/1)
- [Releases](https://github.com/william21c1210-ops/ops-study-maintainer-kit/releases)

## Who this is for

- Beginner DevOps/SRE learners
- Students learning Linux, networking, and cloud basics
- Learners who need reproducible practice evidence for portfolios
- Korean/Japanese learners who want structured technical documentation templates

## Why this project matters

Many beginner learners can run commands, but cannot easily turn practice into reviewable evidence. This project closes that gap by making small DevOps/SRE labs reproducible, testable, and reportable.

The workflow is intentionally simple:

1. run a small lab,
2. collect command output,
3. validate the result,
4. generate a Markdown learning report,
5. keep a public trail of issues, fixes, and releases.

The focus is on operational fundamentals: Linux, networking, cloud basics, validation, and technical documentation. The goal is to help learners build evidence that can be reviewed, repeated, and improved over time.

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

## Documentation and labs

Start here if you are new to the project:

- [Korean beginner quickstart](docs/ko/quickstart.md)
- [Linux grep/find practice lab](examples/linux-grep-find-lab.md)
- [Networking ping vs curl practice lab](examples/networking-ping-vs-curl-lab.md)
- [AWS S3 beginner lab template](templates/aws-s3-beginner-lab.md)
- [AWS S3 evidence example](examples/aws-s3-evidence-example.md)
- [Korean study report template](templates/study-report-ko.md)
- [Japanese study report template](templates/study-report-ja.md)

## Roadmap

The v0.2.0 roadmap was completed through issue-driven PR workflow:

- [x] Linux `grep`/`find` practice lab
- [x] `ping` vs `curl` networking lab
- [x] Korean beginner guide
- [x] AWS S3 beginner lab template
- [x] Japanese report template improvement

Next focus areas include small CLI improvements, additional validation helpers, and more beginner-friendly cloud practice templates.

## Maintainer workflow

This repository is maintained as a learning-oriented OSS project with issues, milestone planning, release notes, CI, tests, and reusable templates. Beginner-friendly issues are used to make future contribution paths easier to understand.

Maintenance work includes:

- issue triage
- documentation updates
- test improvements
- release notes
- beginner contribution review
- automation for report generation and validation

## How Codex and API credits would help

Codex and API credits would directly support maintainer work where speed and consistency matter:

- triaging issues into clear beginner-friendly tasks
- generating small lab templates for Linux, networking, and cloud basics
- reviewing documentation for clarity and reproducibility
- expanding tests around CLI behavior and report generation
- generating study reports from validated lab output
- drafting release notes from completed issues and changes

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. See [LICENSE](LICENSE).
