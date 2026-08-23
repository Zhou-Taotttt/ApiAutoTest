# HTTP 请求客户端。这个文件负责统一处理域名、请求头、Token、超时和GET/POST请求
import requests


class HttpClient:
    def __init__(self, base_url, timeout=15):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {"Accept": "application/json", "Content-Type": "application/json"}
        )

    def set_access_token(self, access_token):
        self.session.headers.update({"Authorization": f"Bearer {access_token}"})

    # 统一请求方法
    def request(self, method, path, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        kwargs.setdefault("timeout", self.timeout)
        return self.session.request(method=method, url=url, **kwargs)

    # 封装GET请求
    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def close(self):
        self.session.close()
