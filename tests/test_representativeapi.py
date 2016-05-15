import requests
import unittest

class TestRepresentativeAPI(unittest.TestCase):
    def setUp(self):
        self.payload = {"address": "185 Berry Street", "key":"AIzaSyDtCedJfTLa9wv62z6-gXJpnPu0NTgnxV0"}
        self.response = requests.get("https://www.googleapis.com/civicinfo/v2/representatives", params=self.payload)

    def test_TrueIfRequestSuccess(self):
        self.assertTrue(self.response.status_code == 200)

    def test_TrueIfResponseIsDict(self):
        self.assertTrue(self.response.json().get("officials"))
