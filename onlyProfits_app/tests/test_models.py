from django.test import TestCase

from onlyProfits_app.models import *

class MarketModelTestCase(TestCase):
    def setUpTestData(cls):
        Market.objects.model.create(ticker="EXAMPLE", values=[5, 4, 3, 2, 1])
    
    def testTickerLabel(self):
        market = Market.objects.get(ticker="EXAMPLE")
        expectedfield_label = market._meta.get_field("ticker").verbose_name
        self.assertEqual(expectedfield_label, "ticker")
    
    def testMaxTickerLabelLength(self):
        market = Market.objects.get(ticker="EXAMPLE")
        expected_max_length = market._meta.get_field("ticker").max_length
        self.assertEqual(expected_max_length, 10)
    
    def testValuesLabel(self):
        market = Market.objects.get(ticker="EXAMPLE")
        field_label = market._meta.get_field("values").verbose_name
        self.assertEqual(field_label, "values")

class OnlyProfitsUserModelTestCase(TestCase):
    def setUpTestData(cls):
        OnlyProfitsUser.objects.model.create(username="test_user", password="test_password", saved_markets=["EXAMPLE2", "EXAMPLE3"])
    
    def testSavedMarketsLabel(self):
        user = OnlyProfitsUser.objects.get(username="test_user")
        expected_field_label = user._meta.get_field("saved_markets").verbose_name
        self.assertEqual(expected_field_label, "saved_markets")
    
    def testUsernameLabelLength(self):
        user = OnlyProfitsUser.objects.get(username="test_user")
        expected_max_length = user._meta.get_field("username").max_length
        self.assertEqual(expected_max_length, 25)
