"""Mosyle Manager Python API"""

from pkg_resources import DistributionNotFound, get_distribution

from .accounts import *
from .actions import *
from .api import *
from .cisco_ise import *
from .classes import *
from .devices import *
from .users import *

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass  # package is not installed
