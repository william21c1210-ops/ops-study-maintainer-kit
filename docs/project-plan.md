# Project Plan

This document keeps the project phases, release strategy, and application-readiness plan explicit.

The goal is to avoid mixing documentation releases, CLI feature releases, external sharing, and the OpenAI Codex OSS support application workflow.

## Strategic positioning

Ops Study Maintainer Kit is not trying to compete with large DevOps roadmap repositories or large interview-question repositories.

Its niche is the evidence layer for beginner DevOps/SRE learners:

> Turn small Linux, networking, and cloud practice into reviewable Markdown evidence.

The project focuses on:

- small reproducible labs,
- command output validation,
- Markdown study reports,
- portfolio-style evidence packs,
- Korean/Japanese beginner-friendly documentation,
- issue-driven OSS maintenance practice.

## Phase map

| Phase | Purpose | Status | Release |
|---|---|---|---|
| Phase 0 | Initial repository, CLI skeleton, tests, CI, issue templates | Done | v0.1.0 |
| Phase 1 | Beginner labs and documentation: Linux, networking, AWS S3, Korean/Japanese resources | Done | v0.2.0 |
| Phase 2 | CLI productization: badges, 60-second demo, resource listing, evidence pack generation | In progress | v0.3.0 |
| Phase 3 | External sharing and feedback collection | Planned | No release required |
| Phase 4 | OpenAI Codex OSS support application final package | Planned | Application step |
| Phase 5 | Post-application improvement: more labs, validation helpers, templates | Planned | v0.4.0+ |

## Release strategy

### v0.1.0 - Initial public release

Purpose:

- establish the repository,
- provide the first CLI skeleton,
- add tests and CI,
- publish the first release.

### v0.2.0 - Beginner labs and documentation

Purpose:

- add beginner-friendly Linux, networking, AWS S3, Korean, and Japanese learning resources,
- close the initial issue/milestone workflow,
- demonstrate issue-driven PR maintenance.

Included:

- Japanese study report template,
- Linux `grep`/`find` practice lab,
- networking `ping` vs `curl` practice lab,
- Korean beginner quickstart,
- AWS S3 beginner lab template,
- AWS S3 evidence example,
- Korean external-sharing draft.

### v0.2.1

Decision:

- skip for now.

Reason:

- the next meaningful release is not a patch release,
- the next step adds real CLI product value,
- `list-resources`, 60-second demo, and evidence pack generation are better grouped into v0.3.0.

### v0.3.0 - Evidence pack generator

Purpose:

- move the project from documentation/labs into a more useful CLI tool,
- support the core positioning as an evidence layer.

Planned/Included:

- README badges,
- 60-second demo,
- `ops-study-kit list-resources`,
- `ops-study-kit new-evidence-pack`,
- tests for resource listing and evidence pack generation,
- README examples for immediate use,
- version metadata update to `0.3.0`.

## Application-readiness checklist

Before submitting to the OpenAI Codex OSS support program, confirm:

- [ ] Public repo is visible without login
- [ ] README clearly explains the project
- [ ] CI badge renders correctly
- [ ] Latest release exists
- [ ] Issues and PRs show real maintainer workflow
- [ ] v0.2.0 release exists
- [ ] v0.3.0 release exists or the latest CLI feature PR is clearly merged
- [ ] No unsupported usage, stars, release asset counts, or contributor claims
- [ ] External sharing post is published or ready to publish
- [ ] GitHub profile README or profile bio points to the project
- [ ] GitHub profile points clearly to this repository
- [ ] Application text explains the project as an early but actively maintained OSS project

## External sharing plan

The external sharing post should request feedback rather than attention metrics.

Use this framing:

> I built a small beginner-friendly DevOps/SRE learning tool that helps learners turn Linux, networking, and AWS practice into reviewable Markdown evidence. It is still early, and I would like feedback from beginner learners.

Recommended platforms:

1. Velog - Korean beginner audience
2. Qiita - Japanese technical audience after Japanese review
3. Zenn - Japanese technical audience after stronger Japanese polish
4. GitHub profile README - project identity and navigation

## What not to do

Do not claim unsupported traction or adoption signals, such as:

- a large user base,
- established community activity,
- download numbers,
- external contributor activity,
- production usage,
- workplace adoption,
- verified visibility.

Do not use artificial engagement or engagement-exchange tactics.

The project should grow through clear usefulness, good documentation, small working CLI features, and honest public sharing.

## Next actions

Current priority order:

1. Finish v0.3.0 CLI productization.
2. Create v0.3.0 release.
3. Update external sharing draft if needed.
4. Publish Korean external sharing post.
5. Create or update GitHub profile README.
6. Prepare the OpenAI Codex OSS support application.
