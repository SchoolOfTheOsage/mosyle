from ..mosyle.devices import Devices, Platforms
from ..settings import Settings

settings = Settings()
settings.load()


def test_read_page():
    devices = Devices()
    devices.read_page(settings.read("access_token"), Platforms.I_OS)
    assert len(devices.devices) > 0


def test_always_fails():
    assert False
