from InfoApiAuto.config.settings import Settings

class HotApi:
    NETWORKS_PATH = Settings.NETWORKS_PATH
    TOP_TOKENS_PATH = Settings.TOP_TOKENS_PATH

    def __init__(self, client):
        self.client = client

    def get_top_tokens_networks(self):
        return self.client.get(self.NETWORKS_PATH)

    def get_top_tokens(self, network):
        params = {"network": network}
        # params=params，是指放在URL查询参数中
        return self.client.get(self.TOP_TOKENS_PATH, params=params)