from InfoApiAuto.config.settings import Settings


class LoginApi:
    LOGIN_PATH = Settings.LOGIN_PATH

    def __init__(self, client):
        self.client = client

    def login(self, email, code):
        payload = {"email": email, "code": code}
        # json=payload 告诉 requests：把字典转换成JSON发送。
        return self.client.post(self.LOGIN_PATH, json=payload)
