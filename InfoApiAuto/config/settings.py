# 公共配置
import os
from dotenv import load_dotenv

# 执行 .env 文件加载
load_dotenv()


class Settings:
    BASE_URL = os.getenv("API_BASE_URL", "")
    LOGIN_PATH = os.getenv("LOGIN_PATH", "")
    NETWORKS_PATH = os.getenv("NETWORKS_PATH", "")
    TOP_TOKENS_PATH = os.getenv("TOP_TOKENS_PATH", "")
    TEST_EMAIL = os.getenv("TEST_EMAIL", "")
    TEST_CODE = os.getenv("TEST_CODE", "")
    REQUEST_TIMEOUT = os.getenv("REQUEST_TIMEOUT", "15")

    @classmethod
    def validate(cls):
        missing = []
        if not cls.BASE_URL:
            missing.append("API_BASE_URL")

        if not cls.TEST_EMAIL:
            missing.append("TEST_EMAIL")

        if not cls.TEST_CODE:
            missing.append("TEST_CODE")

        if missing:
            raise RuntimeError(f".env缺少必要配置：{','.join(missing)}")
