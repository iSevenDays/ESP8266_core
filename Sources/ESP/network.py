# noinspection PyPep8Naming
class network:
    STA_IF = 0
    AP_IF = 1
    network_type = None
    is_active = False

    connected_wifi_ssid = ''
    connected_wifi_password = ''
    connected = False

    essid = None

    @classmethod
    def WLAN(cls, mode) -> 'network':
        n = network()
        n.network_type = mode
        return n

    def active(self, active: bool):
        self.is_active = active

    def connect(self, wifi_ssid, wifi_password):
        self.connected_wifi_ssid = wifi_ssid
        self.connected_wifi_password = wifi_password
        self.connected = True

    def isconnected(self):
        return self.connected

    def ifconfig(self) -> tuple:
        return '192.168.76.6', '255.255.255.0', '192.168.76.1', '192.168.76.1'

    def scan(self) -> list:
        wifi_list = [(b'Bora-Bora', b'\x00\x18\xe7\xfd\xb8\x8a', 3, -64, 4, 0),
                     (b'zeugen1', b'\xac"\x0b\xbb\xb28', 4, -86, 4, 0),
                     (b'Apple', b'\x90\x84\r\xd8\x9c\xd5', 7, -55, 4, 0),
                     (b'lysyi', b'\x00\'",$\xd9', 7, -92, 3, 0),
                     (b'Alova', b'\xa0\xf3\xc1\x9f\xa3<', 8, -80, 3, 0),
                     (b'sanitarium', b'\x90\xf6R\xc8\xe8\x06', 13, -92, 4, 0)]
        return wifi_list

    # Server
    def config(self, essid):
        self.essid = essid