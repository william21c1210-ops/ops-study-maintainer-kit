# AWS S3 Beginner Lab Template

## Purpose

Use this template to document an AWS S3 beginner lab without storing secrets, access keys, or private account information in the repository.

This template is designed for learners who want to turn cloud practice into reviewable evidence.

## Safety rules

- Do not commit AWS access keys, secret keys, session tokens, or account IDs.
- Do not commit screenshots that expose private account information.
- Use placeholder values such as `<bucket-name>` and `<region>`.
- Delete test resources after the lab if they may incur cost.

Even small cloud resources can incur cost. Delete test resources after the lab unless you intentionally want to keep them.

## Lab goal

Describe what you are trying to practice.

Example:

```text
Create an S3 bucket, upload a test file, verify that the file exists, and document the result.
```

## Prerequisites

- AWS account
- AWS CLI installed
- AWS CLI configured locally
- Basic understanding of S3 buckets and objects

## Environment

```text
OS:
AWS CLI version:
Region:
Date:
```

## Prepare a sample file

Linux/macOS/WSL/Git Bash:

```bash
echo "hello s3" > sample.txt
```

Windows PowerShell:

```powershell
"hello s3" | Out-File -Encoding utf8 sample.txt
```

## Commands

Record the commands you ran.

```bash
aws s3 mb s3://<bucket-name> --region <region>
aws s3 cp ./sample.txt s3://<bucket-name>/sample.txt
aws s3 ls s3://<bucket-name>/
```

## Expected result

Write what you expected to see.

```text
The bucket is created.
The sample file is uploaded.
The uploaded object appears in the bucket listing.
```

## Observed result

Paste safe, redacted command output here.

```text
# Redact account IDs, private URLs, and credentials.
```

## Validation checklist

- [ ] I used placeholder or redacted sensitive values.
- [ ] I confirmed the uploaded object appears in S3.
- [ ] I documented the command output.
- [ ] I removed test resources if needed.
- [ ] I did not commit credentials.

## Troubleshooting notes

Common issues:

- Bucket name is already taken.
- AWS CLI is not configured.
- Region is missing or different from expected.
- Permission is denied because IAM permissions are insufficient.
- If bucket deletion fails, check whether objects still remain in the bucket.

## Cleanup

Record cleanup commands if resources should be deleted.

```bash
aws s3 rm s3://<bucket-name>/sample.txt
aws s3 rb s3://<bucket-name>
```

## Portfolio evidence

After completing this lab, learners can document:

- the goal of the S3 practice,
- the commands they ran,
- the validation result,
- how they protected credentials,
- what they cleaned up after the lab.
