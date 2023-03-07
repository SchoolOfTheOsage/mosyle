"""Mosyle Manager Python API - API"""

import requests
from requests.auth import HTTPBasicAuth

REQUEST_URL: str = "https://managerapi.mosyle.com/v2"
REQUEST_HEADERS = {
    "content-type": "application/json",
}
REQUEST_TIMEOUT: int = 60


class ApiClient:
    """API Client"""

    def __init__(
        self,
        access_token: str,
        username: str | None = None,
        password: str | None = None,
    ):
        self.access_token: str = access_token
        self.auth: HTTPBasicAuth | None = None
        if username is not None and password is not None:
            self.auth = HTTPBasicAuth(username, password)

    def post(
        self,
        endpoint: str,
        keys: dict[str, object] | None = None,
        options: dict[str, object] | None = None,
        elements: list[dict[str, object | list[str]]] | None = None,
        filter_options: dict[str, object] | None = None,
    ) -> dict[str, list[object]]:
        """Post Request"""

        payload = keys if keys is not None else {}
        payload["accessToken"] = self.access_token
        if options is not None:
            payload["options"] = options
        if elements is not None:
            payload["elements"] = elements
        if filter_options is not None:
            payload["filterOptions"] = filter_options

        # FIXME: Paging support
        # FIXME: Handle responses other than 200

        response: dict[str, list[object]] = requests.post(
            f"{REQUEST_URL}/{endpoint}",
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
            auth=self.auth,
        ).json()  # ["response"]

        return response
