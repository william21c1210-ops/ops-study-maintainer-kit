# Networking ping vs curl Practice Lab

## Environment

This lab is intended for Linux, macOS, WSL, Git Bash, or another terminal with `ping` and `curl`.

Note:
Command output and ping behavior can differ by operating system. This lab focuses on the mental model, not exact output formatting.

## Goal

Practice the difference between checking network reachability with `ping` and checking HTTP/HTTPS behavior with `curl`.

## Concepts

- `ping`: sends ICMP echo requests to check whether a host responds at the network layer.
- `curl`: sends an application-layer request, often HTTP or HTTPS, and shows the server response.
- ICMP can be blocked even when a website is working.
- A successful `curl` response can show that HTTP/HTTPS is reachable even if `ping` fails.

## Sample target

This lab uses example.com because it is a stable public example domain.

## Practice 1: Check a host with ping

Command:

```bash
ping example.com
```

Expected observation:

```text
You may see replies, latency values, or packet loss.
```

Note:

Some servers block ICMP. If `ping` fails, it does not always mean the website is down.

## Practice 2: Check HTTP headers with curl

Command:

```bash
curl -I https://example.com
```

Explanation:

The `-I` option asks `curl` to fetch only the HTTP response headers.

Expected observation:

```text
HTTP response headers, such as status code and content type.
```

## Practice 3: Compare the results

Record your result:

```text
ping result:
curl result:
What this means:
```

## Common beginner mistake

Wrong mental model:

```text
If ping fails, the website is down.
```

Correct mental model:

```text
ping checks ICMP reachability.
curl checks application-layer HTTP/HTTPS behavior.
A server may block ping while still serving web traffic.
```

## Troubleshooting notes

- If `curl -I` works but `ping` fails, ICMP may be blocked.
- If both fail, there may be a DNS, network, firewall, or server issue.
- If `curl` returns a 4xx or 5xx status code, the server responded but the application may have an error or access rule.

## Portfolio evidence

After completing this lab, learners can document:

- what command they ran,
- whether ICMP worked,
- whether HTTP/HTTPS worked,
- what status code or error they observed,
- how they avoided the “ping failed = server down” mistake.
