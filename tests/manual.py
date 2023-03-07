"""Mosyle Manager Python API - Manual Test"""
import json
import math

import requests
from requests.auth import HTTPBasicAuth

from mosyle.api import REQUEST_HEADERS, REQUEST_URL
from mosyle.configuration.config import Config

CONFIG = Config()
ENDPOINT = "listclasses"
session = requests.Session()
url = f"{REQUEST_URL}/{ENDPOINT}"
session.headers.update(REQUEST_HEADERS)
session.auth = HTTPBasicAuth(CONFIG.username, CONFIG.password)


payload = {elements: []}
