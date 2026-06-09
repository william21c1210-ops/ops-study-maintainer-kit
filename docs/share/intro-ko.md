# IT 초보자가 Linux·Network·AWS 실습을 포트폴리오 기록으로 남기는 방법

## 왜 만들었나

IT 공부를 시작하면 명령어를 따라 치는 일은 비교적 빨리 익숙해집니다. 하지만 시간이 지나면 "무엇을 실행했고, 어떤 결과를 봤고, 그 결과를 어떻게 설명할 수 있는지"를 남기는 일이 더 어렵게 느껴집니다.

Ops Study Maintainer Kit은 이런 기록 과정을 연습하기 위해 만든 초기 공개 프로젝트입니다. 초보 DevOps/SRE 학습자가 Linux, Network, AWS 실습을 reviewable Markdown evidence로 남기도록 돕는 작은 CLI 도구를 목표로 합니다.

## 이 프로젝트가 해결하려는 문제

초보자는 명령어를 실행해도 그 경험을 다시 확인 가능한 기록으로 바꾸는 데서 자주 막힙니다. 예를 들어 터미널에 나온 출력은 지나가면 사라지고, 어떤 개념을 헷갈렸는지도 나중에는 잘 기억나지 않습니다.

이 프로젝트는 실습 주제, 실행한 명령어, 관찰한 출력, 틀린 이해, 수정한 이해를 Markdown 문서로 정리하도록 돕습니다. 포트폴리오에 넣기 위한 완성된 결과물만이 아니라, 학습 과정 자체를 설명 가능한 기록으로 남기는 것이 목표입니다.

## 어떤 실습을 제공하나

첫 번째 예시는 Linux의 `grep`과 `find` 차이입니다. `grep`은 파일 내용에서 문자열을 찾는 명령어이고, `find`는 파일 이름이나 경로 같은 파일 정보를 찾는 명령어입니다. 이 차이를 모르면 "왜 파일 이름은 찾았는데 내용 검색은 안 되지?" 같은 혼란이 생깁니다.

두 번째 예시는 네트워크에서 `ping`과 `curl -I`를 비교하는 실습입니다. `ping`이 실패해도 `curl -I`가 성공하면 서버가 죽은 것이 아니라 ICMP만 차단된 상황일 수 있습니다. 그래서 네트워크 확인을 할 때는 ICMP 응답과 HTTP/HTTPS 응답을 구분해서 기록하는 것이 중요합니다.

세 번째 예시는 AWS S3 evidence 작성입니다. S3 실습 기록에는 credentials, account IDs, private URLs를 남기지 않고 `<bucket-name>`, `<region>` 같은 placeholder를 사용해야 합니다. 실습을 증명하려고 민감한 정보를 저장소에 올리는 것은 피해야 합니다.

## CLI로 할 수 있는 것

현재 제공되는 자료를 먼저 확인할 수 있습니다.

```bash
ops-study-kit list-resources
```

`list-resources`는 현재 저장소에 포함된 docs, labs, templates를 보여줍니다. 처음 보는 사람도 어떤 quickstart, lab, template부터 읽으면 되는지 CLI에서 바로 확인할 수 있습니다.

실습 결과를 evidence pack으로 만들 수도 있습니다.

```bash
ops-study-kit new-evidence-pack --title "Linux grep/find practice" --area linux --output examples/evidence-pack.md
```

`new-evidence-pack`은 목표, 환경, 실행 명령어, 관찰 결과, 검증, 헷갈린 점, 배운 점, 포트폴리오 요약, 다음 실습을 포함한 Markdown evidence pack을 생성합니다. Linux, 네트워크, AWS 같은 기초 실습을 마친 뒤 결과를 정리하는 출발점으로 사용할 수 있습니다.

README에는 설치 후 바로 따라 해볼 수 있는 60-second demo도 있습니다. 짧은 흐름으로 리포트를 만들고, 작은 실습 파일을 검증하고, 결과를 기록으로 남기는 방식을 확인할 수 있습니다.

## 초보자가 얻을 수 있는 것

이 프로젝트를 사용하면 단순히 명령어를 실행하는 데서 끝나지 않고, 아래 내용을 함께 정리할 수 있습니다.

- 어떤 명령어를 실행했는지
- 어떤 파일이나 서비스를 대상으로 했는지
- 어떤 출력을 관찰했는지
- 처음에 어떤 개념을 잘못 이해했는지
- 수정 후 어떤 방식으로 다시 확인했는지
- 포트폴리오나 학습 로그에 어떻게 요약할지
- 다음에 어떤 실습을 이어갈지

이런 기록은 Linux, 네트워크, 클라우드 기초를 공부하는 사람이 자신의 학습 과정을 설명하는 데 도움이 됩니다.

## 현재 포함된 자료

현재 저장소에는 다음 자료와 CLI 기능이 들어 있습니다.

- Linux `grep`/`find` practice lab
- `ping` vs `curl` networking lab
- AWS S3 beginner lab template
- AWS S3 evidence example
- Korean beginner quickstart
- Japanese study report template
- `ops-study-kit list-resources`
- `ops-study-kit new-evidence-pack`

프로젝트 자체도 작은 OSS workflow를 연습하는 형태로 관리하고 있습니다. CI, tests, issues, PR, release를 사용해 작은 변경을 만들고 확인한 뒤 기록으로 남기는 방식을 유지하고 있습니다.

## 아직 초기 프로젝트인 이유

이 저장소는 아직 초기 공개 프로젝트입니다. 자료의 수가 제한적이고, CLI 기능도 더 다듬을 부분이 있습니다. 대신 초보자가 따라 하기 쉬운 구조, 안전한 cloud evidence 작성, 작은 실습을 문서로 남기는 흐름을 먼저 안정적으로 만드는 데 집중하고 있습니다.

## 앞으로 개선할 부분

앞으로는 evidence pack 흐름을 더 자연스럽게 만들고, 추가 validation helper와 cloud 기초 실습 템플릿을 보강하려고 합니다. 한국어와 일본어 문서도 초보자가 따라 읽기 쉬운 방향으로 계속 다듬을 예정입니다.

특히 "실행은 했지만 설명은 못 하겠다"는 상태에서 벗어날 수 있도록, 실습과 기록 사이의 간격을 줄이는 방향으로 개선하려고 합니다.

## 저장소 링크

저장소는 아래에서 볼 수 있습니다.

https://github.com/william21c1210-ops/ops-study-maintainer-kit

초기 프로젝트라 부족한 점이 많습니다. Linux, 네트워크, AWS 기초를 공부하는 초보자 관점에서 더 필요한 실습이나 문서가 있다면 피드백을 받고 싶습니다.
