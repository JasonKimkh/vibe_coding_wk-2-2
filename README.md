# 🛍️ LangGraph Agent 상품 검색 챗봇

> LangGraph Agent를 활용한 지능형 상품 검색 챗봇 프로젝트  
> FastAPI 백엔드 + Streamlit 프론트엔드 + AI Agent 아키텍처

[![GitHub Issues](https://img.shields.io/github/issues/JasonKimkh/vibe_coding_wk-2-2)](https://github.com/JasonKimkh/vibe_coding_wk-2-2/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/JasonKimkh/vibe_coding_wk-2-2)](https://github.com/JasonKimkh/vibe_coding_wk-2-2/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📋 프로젝트 개요

이 프로젝트는 LangGraph React Agent를 사용하여 사용자의 자연어 질문을 이해하고, DuckDuckGo를 통해 웹 검색을 수행하여 상품 정보를 제공하는 지능형 챗봇입니다.

### 🎯 주요 기능

- 🤖 **지능형 상품 검색**: 자연어 질문을 이해하고 적절한 상품 정보 제공
- 🔍 **실시간 웹 검색**: DuckDuckGo API를 통한 최신 상품 정보 수집
- 💬 **직관적인 채팅 인터페이스**: Streamlit 기반의 사용자 친화적 UI
- 🚀 **고성능 API**: FastAPI 기반의 비동기 처리
- 📊 **AI 모니터링**: LangSmith 연동을 통한 AI Agent 성능 추적

## 🏗️ 시스템 아키텍처

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │    FastAPI      │    │   LangGraph     │
│   Frontend      │◄──►│    Backend      │◄──►│    Agent        │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
                                               ┌─────────────────┐
                                               │  DuckDuckGo     │
                                               │  Search Tool    │
                                               └─────────────────┘
```

## 🛠️ 기술 스택

### 백엔드
- **FastAPI**: 고성능 비동기 웹 프레임워크
- **Python 3.11**: 최신 Python 기능 활용
- **Uvicorn**: ASGI 서버

### AI & ML
- **LangGraph**: AI Agent 프레임워크
- **LangChain**: LLM 애플리케이션 개발 도구
- **Gemini-2.5-flash-preview**: Google의 최신 LLM 모델
- **LangSmith**: AI Agent 모니터링 및 디버깅

### 프론트엔드
- **Streamlit**: 빠른 웹 앱 개발 프레임워크

### 개발 도구
- **pytest**: 테스트 프레임워크
- **GitHub Actions**: CI/CD 자동화
- **flake8**: 코드 품질 검사

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/JasonKimkh/vibe_coding_wk-2-2.git
cd vibe_coding_wk-2-2
```

### 2. 환경 설정
```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate     # Windows

# 의존성 설치
cd backend
pip install -r requirements.txt
```

### 3. 환경 변수 설정
`.env` 파일을 생성하고 다음 내용을 추가:
```env
GOOGLE_API_KEY=your_gemini_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
```

### 4. 서버 실행

#### 백엔드 서버 시작
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### 프론트엔드 서버 시작
```bash
cd frontend
streamlit run app.py
```

### 5. 접속
- **프론트엔드**: http://localhost:8501
- **백엔드 API**: http://localhost:8000
- **API 문서**: http://localhost:8000/docs

## 📁 프로젝트 구조

```
vibe_coding_wk-2-2/
├── backend/                     # FastAPI 백엔드
│   ├── app/
│   │   ├── api/                # API 라우터
│   │   ├── services/           # 비즈니스 로직
│   │   ├── agents/             # AI Agent 구현
│   │   └── main.py            # FastAPI 앱 엔트리포인트
│   ├── tests/                  # 테스트 코드
│   └── requirements.txt        # Python 의존성
├── frontend/                    # Streamlit 프론트엔드
│   ├── app.py                  # Streamlit 앱
│   └── requirements.txt        # Frontend 의존성
├── .github/                     # GitHub 설정
│   ├── workflows/              # GitHub Actions
│   ├── ISSUE_TEMPLATE/         # 이슈 템플릿
│   └── pull_request_template.md
├── docs/                        # 프로젝트 문서
├── .cursor/rules/              # 개발 가이드라인
└── README.md                   # 프로젝트 설명
```

## 🧪 테스트

```bash
# 백엔드 테스트 실행
cd backend
pytest tests/ -v

# 코드 품질 검사
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## 🤝 기여하기

프로젝트에 기여해주셔서 감사합니다! 

### 기여 방법
1. 이 저장소를 Fork하세요
2. 새로운 기능 브랜치를 생성하세요 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋하세요 (`git commit -m 'Add some amazing feature'`)
4. 브랜치에 푸시하세요 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성하세요

### 개발 가이드라인
- [개발 원칙](/.cursor/rules/development-policy.mdc)
- [코딩 컨벤션](/.cursor/rules/project-structure.mdc)
- [GitHub 관리 규칙](/.cursor/rules/github-management.mdc)

## 📈 GitHub Actions

이 프로젝트는 다음과 같은 자동화된 워크플로우를 제공합니다:

- ✅ **자동 테스트**: PR/Push 시 테스트 자동 실행
- 🏷️ **자동 라벨링**: 파일 변경사항에 따른 라벨 자동 추가
- 👥 **자동 할당**: 코드 소유자 기반 리뷰어 자동 할당
- 💬 **자동 댓글**: PR/이슈 생성 시 가이드 메시지 추가
- 🔍 **자동 리뷰**: 코드 변경사항 분석 및 권장사항 제공

## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 📞 문의

- **이슈**: [GitHub Issues](https://github.com/JasonKimkh/vibe_coding_wk-2-2/issues)
- **토론**: [GitHub Discussions](https://github.com/JasonKimkh/vibe_coding_wk-2-2/discussions)

---

⭐ 이 프로젝트가 도움이 되었다면 스타를 눌러주세요! 