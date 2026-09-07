# Gemini Quota Monitor

Termux와 Python에서 사용할 수 있는 Gemini API Quota Monitor 프로젝트입니다.

이 프로젝트는 Gemini API 키를 메인 코드와 분리하여 관리하도록 만들어졌습니다.

---

## 📁 프로젝트 구조

```text
gemini-quota-monitor/
├── quota_monitor.py
├── api_key.py
├── api_key_example.py
├── requirements.txt
├── .gitignore
└── README.md
```

### 파일 설명

| 파일                   | 설명                             |
| -------------------- | ------------------------------ |
| `quota_monitor.py`   | 프로그램의 메인 파일                    |
| `api_key.py`         | 실제 Gemini API 키를 저장하는 파일       |
| `api_key_example.py` | API 키 파일 예시                    |
| `requirements.txt`   | 필요한 Python 라이브러리 목록            |
| `.gitignore`         | API 키 파일이 GitHub에 업로드되지 않도록 설정 |
| `README.md`          | 프로젝트 설명 및 사용 방법                |

---

# ⚠️ 중요

`api_key.py`에는 실제 Gemini API 키가 들어갑니다.

이 파일은 절대로 GitHub에 업로드하면 안 됩니다.

`.gitignore`에 다음 설정이 포함되어 있습니다.

```gitignore
api_key.py
```

따라서 GitHub에는 API 키가 없는 `api_key_example.py`만 업로드합니다.

---

# 💻 컴퓨터에서 사용하기

프로젝트 폴더로 이동합니다.

```bash
cd gemini-quota-monitor
```

API 키 파일을 생성합니다.

```bash
cp api_key_example.py api_key.py
```

그다음 `api_key.py`를 열어 Gemini API 키를 입력합니다.

```python
GEMINI_API_KEY = "여기에_API_키를_입력"
```

프로그램을 실행합니다.

```bash
python quota_monitor.py
```

---

# 📱 Termux 설치 방법

Termux에서 필요한 프로그램을 설치합니다.

```bash
pkg update
pkg install git python nano
```

GitHub 저장소를 다운로드합니다.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

프로젝트 폴더로 이동합니다.

```bash
cd gemini-quota-monitor
```

API 키 파일을 생성합니다.

```bash
cp api_key_example.py api_key.py
```

API 키 파일을 수정합니다.

```bash
nano api_key.py
```

다음과 같이 Gemini API 키를 입력합니다.

```python
GEMINI_API_KEY = "AIza..."
```

저장한 후 프로그램을 실행합니다.

```bash
python quota_monitor.py
```

---

# 🔐 API 키 관리

API 키는 다음 파일에 저장합니다.

```text
api_key.py
```

예시:

```python
GEMINI_API_KEY = "AIza..."
```

메인 프로그램인 `quota_monitor.py`는 다음 방식으로 API 키를 읽습니다.

```python
from api_key import GEMINI_API_KEY
```

따라서 API 키를 변경하고 싶을 때는 메인 프로그램을 수정할 필요가 없습니다.

다음 명령어만 사용하면 됩니다.

```bash
nano api_key.py
```

API 키를 수정한 뒤 저장하고 프로그램을 다시 실행하면 새로운 키가 적용됩니다.

---

# 🛡️ 보안

다음 파일은 GitHub에 업로드하지 않습니다.

```text
api_key.py
.env
credentials.json
token.json
```

API 키가 실수로 GitHub에 올라가지 않도록 `.gitignore`를 확인하세요.

---

# 🚀 현재 기능

현재 버전에서는 다음 기능을 제공합니다.

* `api_key.py`에서 Gemini API 키 읽기
* API 키 파일 존재 여부 확인
* API 키가 비어 있는지 확인
* API 키를 전체 공개하지 않고 일부만 표시
* Termux에서 실행 가능
* 컴퓨터에서 개발 후 GitHub를 통해 Termux로 배포 가능

---

# 🔮 앞으로 추가할 기능

다음 기능을 추가할 예정입니다.

* Google Cloud Quota 정보 조회
* Gemini 관련 Quota 자동 탐색
* 사용량 정보 표시
* 요청 제한 상태 표시
* 실시간 화면 갱신
* 마지막 업데이트 시간 표시
* Termux에서 간편하게 실행하는 명령어 추가

---

# 🔄 개발 및 배포 방식

프로젝트는 다음과 같은 방식으로 개발할 수 있습니다.

```text
컴퓨터
   │
   │ 코드 개발
   ▼
GitHub
   │
   │ git clone / git pull
   ▼
Termux
```

컴퓨터에서 코드를 수정한 뒤 GitHub에 업로드합니다.

```bash
git add .
git commit -m "Update"
git push
```

Termux에서는 프로젝트 폴더에서 다음 명령어로 최신 버전을 받을 수 있습니다.

```bash
git pull
```

그 후 다시 실행합니다.

```bash
python quota_monitor.py
```

---

# 📌 주의사항

이 프로젝트는 API 키를 코드에 직접 입력하지 않고 별도의 파일에서 관리합니다.

`api_key.py` 파일은 개인 정보에 해당할 수 있으므로 다른 사람과 공유하거나 GitHub에 업로드하지 마세요.
