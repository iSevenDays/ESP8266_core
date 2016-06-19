from enum import Enum

from .ESPClient import ESPClient


class ESPCore:
    class WiFiMode(Enum):
        AP = 0
        STA_AP = 1

    mode = None
    client = None
    server = None

    def __init__(self, mode: WiFiMode, home_wifi_ssid, home_wifi_password):
        self.mode = mode
        self.client = ESPClient(home_wifi_ssid, home_wifi_password)

