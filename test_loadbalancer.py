import pytest
from loadbalancer import lb
import werkzeug


@pytest.fixture
def client():
    with lb.test_client() as client:
        yield client


def test_host_mango_routing(client):
    result = client.get("/", headers={'HOST': "www.mango.com"})
    assert b'This is mango server' == result.data


def test_host_apple_routing(client):
    result = client.get("/", headers={'HOST': "www.apple.com"})
    assert b'This is apple server' == result.data


def test_host_routing_not_found(client):
    result = client.get("/", headers={'HOST': "www.notamango.com"})
    assert b'not found' in result.data
    assert 404 == result.status_code


def test_path_routing_mango(client):
    result = client.get("/mango")
    assert b'This is mango server' == result.data


def test_path_routing_apple(client):
    result = client.get("/apple")
    assert b'This is apple server' == result.data
