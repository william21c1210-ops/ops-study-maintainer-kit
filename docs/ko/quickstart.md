# 한국어 초보자 가이드

## 이 문서의 목적

이 문서는 Linux, 네트워킹, 그리고 앞으로 추가될 클라우드 기초를 공부하는 한국어권 초보자가 이 프로젝트를 사용해 실습 결과를 재현 가능한 evidence로 남기는 방법을 설명합니다.

## 이 프로젝트로 할 수 있는 것

- 실습 주제별 Markdown 학습 리포트 만들기
- Linux/networking 실습 결과를 정리하고, 향후 cloud 기초 실습으로 확장하기
- 어떤 명령어를 실행했고 어떤 결과를 확인했는지 기록하기
- 포트폴리오에 넣을 수 있는 학습 evidence 만들기

## 필요한 준비물

- Git
- Python 3.10 이상
- Windows 사용자는 PowerShell, WSL, 또는 Git Bash
- Linux/macOS 사용자는 기본 터미널

## 설치

### Windows PowerShell

```powershell
git clone https://github.com/william21c1210-ops/ops-study-maintainer-kit.git
cd ops-study-maintainer-kit
python -m venv .venv
.\.venv\Scripts\activate
pip install -e ".[dev]"
```

### Linux/macOS/WSL

```bash
git clone https://github.com/william21c1210-ops/ops-study-maintainer-kit.git
cd ops-study-maintainer-kit
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## 첫 번째 리포트 만들기

```powershell
ops-study-kit new-report --title "Linux grep and find practice" --output examples/my-report.md
```

Note:
`ops-study-kit` 명령이 인식되지 않으면 가상환경이 활성화되어 있는지 먼저 확인하세요.

## 파일 내용 검증하기

```powershell
ops-study-kit check-text --file examples/linux-grep-find-sample.log --contains ERROR
```

## 추천 학습 순서

1. `examples/linux-grep-find-lab.md` 읽기
2. `examples/linux-grep-find-sample.log`로 실습하기
3. `examples/networking-ping-vs-curl-lab.md` 읽기
4. 내 결과를 Markdown 리포트로 정리하기
5. 틀린 개념을 수정해서 다시 기록하기

## 초보자가 자주 헷갈리는 부분

### `find`와 `grep`

- `find`: 파일 이름, 경로, 파일 종류를 찾는 명령어
- `grep`: 파일 안의 문자열을 찾는 명령어

### `ping`과 `curl`

- `ping`: ICMP 응답을 확인
- `curl`: HTTP/HTTPS 응답을 확인

`ping`이 실패해도 `curl`이 성공할 수 있습니다. 이 경우 서버가 ICMP를 차단했을 수 있습니다.

## 포트폴리오 evidence로 남길 것

- 실행한 명령어
- 사용한 파일
- 관찰한 출력
- 처음에 헷갈린 개념
- 수정한 이해
- 다음 실습 계획

## 다음 단계

- Linux 명령어 실습 추가
- 네트워킹 기본 개념 정리
- AWS S3 같은 클라우드 기초 실습 템플릿 추가 예정
- 한국어/일본어 기술 문서 템플릿 개선
