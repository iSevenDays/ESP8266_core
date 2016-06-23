from Sources.ESP.network import network


class ESPServer:
    wifi_ssid = None
    wifi_password = None

    internal_ap = network.WLAN(network.AP_IF)

    def __init__(self, wifi_ssid, wifi_password=None):
        self.wifi_ssid = wifi_ssid
        self.wifi_password = wifi_password

    def start_ap(self):
        self.internal_ap.active(True)

    def isconnected(self):
        return self.internal_ap.isconnected()
