from InfoApiAuto.config.settings import Settings


class CollectedTokensApi:
    COLLECTED_TOKENS_PATH = Settings.COLLECTED_TOKENS_PATH

    def __init__(self, client):
        self.client = client

    def collect_token(self, network, address):
        payload = {"network": network, "address": address}
        # json=payload，是指将参数放到json请求体中
        return self.client.post(self.COLLECTED_TOKENS_PATH, json=payload)

    def cancel_collect_token(self, network, address):
        payload = {"network": network, "address": address}
        return self.client.delete(self.COLLECTED_TOKENS_PATH, json=payload)