# tests/test_dummy_live.py
import pytest
import requests


@pytest.mark.integration
def test_dummy_ping_live():
    r = requests.post("http://127.0.0.1:8000/plugins/dummy/ping", json={"hello": "world"})
    assert r.status_code == 200
