import base64


class Authorization:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def to_string(self) -> str:
        plaintext_auth = self.username + ":" + self.password
        base64_auth = base64.b64encode(plaintext_auth.encode()).decode()
        return f"Basic {base64_auth}"
