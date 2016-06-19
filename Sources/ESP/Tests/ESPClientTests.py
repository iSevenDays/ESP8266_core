from unittest import TestCase

from Sources.ESP.ESPClient import ESPClient


class ESPClientTests(TestCase):
    def test_connect_to_home_wifi(self):
        client = ESPClient('', '')
        client.connect_to_home_wifi()
        self.assertTrue(client.isconnected())

    def test_returns_ip_address(self):
        client = ESPClient('', '')
        ip_address = client.ip_address()
        self.assertEqual(ip_address, '192.168.76.6')

    def test_scans_network(self):
        client = ESPClient('', '')
        scan_results = client.scan()
        self.assertEqual(len(scan_results), 6)
