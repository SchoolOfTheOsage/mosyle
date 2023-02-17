class CiscoIseOperation:
    """Cisco ISE Operation Types"""

    ADD = "add"
    REMOVE = "remove"


def _cisco_ise_operations(
    self, action: str, wifi_mac: str, serial_number: str, model: str | None = None
):
    url = f"{REQUEST_URL}/ciscoise"

    element: dict[str, object] = {
        "action": action,
        "wifimac": wifi_mac,
        "serialnumber": serial_number,
    }
    if model is not None:
        element["model"] = model

    payload = {
        "accessToken": self.access_token,
        "elements": [element],
    }

    return requests.post(
        url,
        json=payload,
        headers=REQUEST_HEADERS,
        timeout=REQUEST_TIMEOUT,
        auth=self.auth,
    ).json()
