# Linux grep/find Practice Lab

## Environment

This lab is intended for Linux, macOS, WSL, or Git Bash.

## Goal

Practice the difference between finding files and searching inside files.

## Concepts

- `find`: searches for files and directories by name, path, type, or other file metadata.
- `grep`: searches inside file contents.
- `|` pipe: sends the output lines from the left command into the right command.
- `$()` command substitution: runs a command first and inserts its output into another command.

## Sample file

Use `examples/linux-grep-find-sample.log`.

## Practice 1: Search inside one file with grep

Command:

```bash
grep -i "error" examples/linux-grep-find-sample.log
```

Expected result:

```text
ERROR database connection failed
error timeout while reading cache
```

## Practice 2: Find log files

Command:

```bash
find examples -name "*.log"
```

Expected result should include:

```text
examples/linux-grep-find-sample.log
```

## Practice 3: Use command substitution

Command:

```bash
grep -i "error" $(find examples -name "*.log")
```

Explanation:
`find` runs first and returns matching log file paths. Then `grep` searches inside those files.

## Practice 4: Pipe output into another command

Command:

```bash
find examples -name "*.log" | wc -l
```

Explanation:
The pipe sends the list of found log files into `wc -l`, which counts lines.

Note:
The wc -l example is intended for Linux, macOS, WSL, or Git Bash environments.

## Common beginner mistake

Wrong mental model:

```text
grep finds file names.
```

Correct mental model:

```text
find finds file paths.
grep searches file contents.
```

## Portfolio evidence

After completing this lab, learners can document:

- what command they ran,
- what output they observed,
- whether they searched file names or file contents,
- how they corrected a wrong mental model.
