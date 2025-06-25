from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat

# GitHub Actions 테스트를 위한 FastAPI 애플리케이션
app = FastAPI(
    title="Chat API",
    description="간단한 채팅 API 서버 - GitHub Actions 테스트 중",
    version="1.0.1"  # 버전 업데이트
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(chat.router)


@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {
        "message": "Chat API Server", 
        "status": "GitHub Actions 테스트 중",
        "version": "1.0.1"
    }


@app.get("/health")
async def health_check():
    """헬스체크 엔드포인트"""
    return {"status": "healthy"}


@app.get("/test")
async def test_endpoint():
    """GitHub Actions 테스트를 위한 새로운 엔드포인트"""
    return {
        "message": "테스트 엔드포인트입니다",
        "purpose": "GitHub Actions 워크플로우 테스트",
        "features": [
            "자동 테스트 실행",
            "자동 라벨링",
            "자동 리뷰어 할당",
            "자동 댓글 추가"
        ]
    } 