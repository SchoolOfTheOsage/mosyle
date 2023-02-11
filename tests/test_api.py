from api import Api


def test_api_default():
    api = Api()
    assert isinstance(api, Api)
