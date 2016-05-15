import unittest
import re

class TestZipCodeValidation(unittest.TestCase):
    def setUp(self):
        self.p = re.compile("^\d{5}(-\d{4})?$")

    def test_FalseIfLessThanFiveDigits(self):
        self.assertFalse(self.p.match("4904"))

    def test_FalseIfMoreThanFiveDigitsAndNoHyphen(self):
        self.assertFalse(self.p.match("4900004"))

    def test_TrueIfFiveDigits(self):
        self.assertTrue(self.p.match("49004"))

    def test_TrueIfNineDigitsWithHyphen(self):
        self.assertTrue(self.p.match("49004-7485"))

    def test_FalseIfNineDigitsWithNoHyphen(self):
        self.assertFalse(self.p.match("490999999"))

    def test_FalseIfLessThanFourNumbersAfterHyphen(self):
        self.assertFalse(self.p.match("49004-43"))

    def test_FalseIfMoreThanFourNumbersAfterHyphen(self):
        self.assertFalse(self.p.match("49004-34344"))

    def test_FalseIfHyphenWithNoFrontDigits(self):
        self.assertFalse(self.p.match("-4348"))

    def test_FalseIfNoDigitsAfterHyphen(self):
        self.assertFalse(self.p.match("49004-"))

    def test_FalseIfLessThanFiveFrontDigits(self):
        self.assertFalse(self.p.match("2-4535"))

    def test_TrueIfAllZeros(self):
        self.assertTrue(self.p.match("00000"))
        self.assertTrue(self.p.match("00000-0000"))