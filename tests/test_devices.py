from ..mosyle.devices.devices import Devices, Platforms
from ..settings import Settings

settings = Settings()
settings.load()


def test_read():
    devices = Devices()
    devices.read(
        settings.read("access_token"),
        Platforms.I_OS,
    )
    assert len(devices.devices) > 0
