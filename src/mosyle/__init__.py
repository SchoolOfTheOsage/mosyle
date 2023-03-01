"""Mosyle Manager Python API"""

from pkg_resources import DistributionNotFound, get_distribution

from .account import *
from .action import *
from .api_client import *
from .cisco_ise import *
from .device import *
from .section import *
from .user import *

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass  # package is not installed
