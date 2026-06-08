# AWS S3 Evidence Example

This is a documentation example only. It is not proof that the commands were executed against a real AWS account.

This is an example format for documenting an S3 practice lab. It does not contain real credentials, account IDs, or private infrastructure details.

## Lab summary

Goal:
Create a test S3 bucket, upload a sample file, and verify the object listing.

## Redacted environment

```text
OS: Windows / WSL / Linux / macOS
AWS CLI version: aws-cli/2.x.x
Region: <region>
Date: YYYY-MM-DD
```

## Commands used

```bash
aws s3 mb s3://<bucket-name> --region <region>
aws s3 cp ./sample.txt s3://<bucket-name>/sample.txt
aws s3 ls s3://<bucket-name>/
```

## Safe output example

```text
make_bucket: <bucket-name>
upload: ./sample.txt to s3://<bucket-name>/sample.txt
2026-01-01 00:00:00         12 sample.txt
```

## What this proves

- The learner can create an S3 bucket.
- The learner can upload an object.
- The learner can verify the result with AWS CLI.
- The learner can redact sensitive values before committing evidence.

## Cleanup note

Learners should remove test resources if they may incur cost.
