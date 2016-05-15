import unittest
import lob

class TestLobAPI(unittest.TestCase):
    def setUp(self):
      lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

    def test_TrueIfStateListIsDict(self):
        states = lob.State.list()
        self.assertTrue(states.get("data"))

    def test_TrueIfLetterIsDict(self):
        letter = lob.Letter.create(
            description = 'Demo Letter',
        to_address = {
              'name': 'Harry Zhang',
              'address_line1': '123 Test Street',
              'address_city': 'Mountain View',
              'address_state': 'CA',
              'address_zip': '94041',
              'address_country': 'US'
          },
          from_address = {
              'name': 'Harry Zhang',
              'address_line1': '123 Test Avenue',
              'address_line2': 'Suite 107',
              'address_city': 'Seattle',
              'address_state': 'WA',
              'address_zip': '94041',
              'address_country': 'US'
          },
          file = '<html style="padding-top: 3in; margin: .5in;">{{message}}</html>',
          data = {
            'message': "This is a test letter for Lob's coding challenge. Thank you legislator."
          },
          color = True)
        self.assertTrue(letter.get("url"))