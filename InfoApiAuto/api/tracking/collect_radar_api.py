from InfoApiAuto.config.settings import Settings


class CollectRadarApi:
    COLLECT_RADAR_PATH = Settings.COLLECT_RADAR_PATH

    def __init__(self, client):
        self.client = client

    def get_collect_radar(self):
        return self.client.get(self.COLLECT_RADAR_PATH)