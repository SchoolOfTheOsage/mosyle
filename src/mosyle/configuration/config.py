"""Mosyle Manager Python API - Configuration"""
import configparser
import os


class Config:
    """Configuration"""

    def __init__(self, section: str = "DEFAULT"):
        self.config = configparser.ConfigParser()
        home = os.path.expanduser("~")
        config_dir = f"{home}/.mosyle"
        if not os.path.isfile(config_dir):
            os.makedirs(config_dir, exist_ok=True)
        self.config_file = f"{config_dir}/config.ini"
        self.config.read(self.config_file)
        self.section = section

    def _get(self, option: str) -> str:
        if self.config.has_option(self.section, option):
            return self.config[self.section][option]
        return ""

    def _set(self, option: str, value: str):
        self.config[self.section][option] = value
        self.config.write(open(self.config_file, "w", encoding="utf-8"))

    @property
    def token(self) -> str:
        """Get API Token"""
        return self._get("token")

    @token.setter
    def token(self, token: str):
        """Set API Token"""
        self._set("token", token)

    @property
    def token_obfuscated(self) -> str:
        """Get API Token Obfuscated"""
        return f"{self.token[:4]}...{self.token[-4:]}"

    @token_obfuscated.setter
    def token_obfuscated(self, token: str):
        """Set API Token Obfuscated"""
        if token != self.token_obfuscated:
            self.token = token

    @property
    def username(self) -> str:
        """Get API Username"""
        return self._get("username")

    @username.setter
    def username(self, username: str):
        """Set API Username"""
        self._set("username", username)

    @property
    def password(self) -> str:
        """Get API Password"""
        return self._get("password")

    @password.setter
    def password(self, password: str):
        """Set API Password"""
        self._set("password", password)

    @property
    def password_obfuscated(self) -> str:
        """Get API Password Obfuscated"""
        return "*******"

    @password_obfuscated.setter
    def password_obfuscated(self, password: str):
        """Set API Password Obfuscated"""
        if password != self.password_obfuscated:
            self.password = password
