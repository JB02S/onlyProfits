from django.test import TestCase

from onlyProfits_app.models import *

class MarketModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Market.objects.create(ticker="EXAMPLE", values=[5, 4, 3, 2, 1])
    
    def test_ticker_label(self):
        market = Market.objects.get(ticker="EXAMPLE")
        expectedfield_label = market._meta.get_field("ticker").verbose_name
        self.assertEqual(expectedfield_label, "ticker")
    
    def test_max_ticker_label_length(self):
        market = Market.objects.get(ticker="EXAMPLE")
        expected_max_length = market._meta.get_field("ticker").max_length
        self.assertEqual(expected_max_length, 10)
    
    def test_values_label(self):
        market = Market.objects.get(ticker="EXAMPLE")
        field_label = market._meta.get_field("values").verbose_name
        self.assertEqual(field_label, "values")

class OnlyProfitsUserModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="test_user", password="test_password")
        OnlyProfitsUser.objects.create(django_user=user, saved_markets=["EXAMPLE2", "EXAMPLE3"])
    
    def test_saved_markets_label(self):
        user = OnlyProfitsUser.objects.get(django_user=User.objects.get(username='test_user'))
        expected_field_label = user._meta.get_field("saved_markets").verbose_name
        self.assertEqual(expected_field_label, "saved markets")
    
    def test_username_label_length(self):
        user = OnlyProfitsUser.objects.get(django_user=User.objects.get(username='test_user'))
        expected_max_length = user.django_user._meta.get_field("username").max_length
        self.assertEqual(expected_max_length, 25)
