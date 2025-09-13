# tests/test_dummy_live.py
import pytest
import requests


@pytest.mark.integration
def test_dummy_ping_live():
    """Integration test: requires a running server on localhost:8000."""
    r = requests.post("http://127.0.0.1:8000/plugins/dummy/ping", json={"hello": "world"})
    assert r.status_code == 200

    data = r.json()
    assert data["plugin"] == "dummy"
    assert data["result"]["task"] == "ping"
    assert data["result"]["payload_received"]["hello"] == "world"
