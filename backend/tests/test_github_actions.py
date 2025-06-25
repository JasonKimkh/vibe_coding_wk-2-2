"""
GitHub Actions 워크플로우 테스트를 위한 테스트 케이스
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """루트 엔드포인트 테스트"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert "version" in data
    assert data["version"] == "1.0.1"


def test_health_check():
    """헬스체크 엔드포인트 테스트"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_new_test_endpoint():
    """새로 추가된 테스트 엔드포인트 테스트"""
    response = client.get("/test")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "purpose" in data
    assert "features" in data
    assert isinstance(data["features"], list)
    assert len(data["features"]) == 4
    
    # 버그 수정 후 새로 추가된 필드들 테스트
    assert "bug_introduced" in data
    assert "error_count" in data
    assert "error_status" in data
    assert data["bug_introduced"] is False  # 버그가 수정됨
    assert isinstance(data["error_count"], int)  # 정수 타입
    assert data["error_count"] == 0  # 오류 개수 0
    assert data["error_status"] == "resolved"  # 해결 상태


def test_github_actions_features():
    """GitHub Actions 기능 테스트"""
    response = client.get("/test")
    data = response.json()
    
    expected_features = [
        "자동 테스트 실행",
        "자동 라벨링", 
        "자동 리뷰어 할당",
        "자동 댓글 추가"
    ]
    
    for feature in expected_features:
        assert feature in data["features"]


@pytest.mark.parametrize("endpoint", ["/", "/health", "/test"])
def test_all_endpoints_return_json(endpoint):
    """모든 엔드포인트가 JSON을 반환하는지 테스트"""
    response = client.get(endpoint)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json" 