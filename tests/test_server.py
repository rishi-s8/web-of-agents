from fastapi.testclient import TestClient
from webofagents.node.server import app

client = TestClient(app)

def test_get_handshake():
    """Test if the root endpoint returns the correct specification sheet."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "title": "AI Agents Collaboration Network",
        "version": "1.0",
        "description": "A modular platform for AI agents to communicate and collaborate effectively."
    }