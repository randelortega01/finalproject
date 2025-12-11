"""
Unit tests for the Flask application routes
"""
import pytest
from service import app


@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestIndexRoute:
    """Tests for the index route"""

    def test_index_returns_200(self, client):
        """Test that index returns 200 status"""
        response = client.get("/")
        assert response.status_code == 200

    def test_index_returns_welcome_message(self, client):
        """Test that index returns correct message"""
        response = client.get("/")
        data = response.get_json()
        assert data["message"] == "Welcome to the CI/CD Final Project"
        assert data["status"] == 200


class TestHealthRoute:
    """Tests for the health route"""

    def test_health_returns_200(self, client):
        """Test that health endpoint returns 200"""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_healthy(self, client):
        """Test that health endpoint returns healthy status"""
        response = client.get("/health")
        data = response.get_json()
        assert data["message"] == "Healthy"


class TestInfoRoute:
    """Tests for the info route"""

    def test_info_returns_200(self, client):
        """Test that info endpoint returns 200"""
        response = client.get("/info")
        assert response.status_code == 200

    def test_info_returns_correct_data(self, client):
        """Test that info endpoint returns application info"""
        response = client.get("/info")
        data = response.get_json()
        assert data["name"] == "CI/CD Final Project"
        assert data["version"] == "1.0.0"


class TestCountRoute:
    """Tests for the count route"""

    def test_count_returns_200(self, client):
        """Test that count endpoint returns 200"""
        response = client.get("/count")
        assert response.status_code == 200

    def test_count_returns_number(self, client):
        """Test that count endpoint returns a count"""
        response = client.get("/count")
        data = response.get_json()
        assert "count" in data
        assert isinstance(data["count"], int)

