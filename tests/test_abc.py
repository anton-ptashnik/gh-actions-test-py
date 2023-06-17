import pytest
import requests


def test_thing1():
    r=requests.get('http://httpbin.org')
    assert r.status_code == 200


@pytest.mark.asyncio
async def test_thing2():
    pass
