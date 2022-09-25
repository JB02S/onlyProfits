from typing import Dict

from django.test import TestCase
from django.urls import reverse
# from django.contrib.auth.models import User
from onlyProfits_app.models import Market, OnlyProfitsUser, User
import json

class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="test_user", password="test_password")
        for i in range(5):
            Market.objects.create(ticker="EXAMPLE" + str(i), values=[i, i + 3, i + 2, i + 4, i + 5], volume=66666)
    
    def test_check_template(self):
        self.assertTemplateUsed(self.client.get("onlyProfits:/"), "onlyProfits_app/onlyProfits.html")
    
    def test_context_dictionary(self):
        response = self.client.get(reverse("onlyProfits_app:index"))
        expected_markets = Market.objects.order_by("volume")
        self.assertEqual(response.context["markets"], expected_markets)
        self.assertTrue("markets" in response.context)


class CreateAccountViewTest(TestCase):
    def test_check_template(self):
        self.assertTemplateUsed(self.client.get("onlyProfits:/create_account"), "onlyProfits_app/create_account.html")
    
    def test_context_dictionary(self):
        self.assertIsNone(self.client.get(reverse("onlyProfits_app:create_account")).context)


class AccountViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            Market.objects.create(ticker="EXAMPLE" + str(i), values=[i, i + 3, i + 2, i + 4, i + 5], volume=66666)
        User.objects.create(username="test_user", password="test_password", saved_markets=["EXAMPLE1", "EXAMPLE2"])
    
    def test_check_template(self):
        self.assertTemplateUsed(self.client.get("onlyProfits:/account/test_user"), "onlyProfits_app/account.html")
    
    def test_context_dictionary(self):
        response = self.client.get(reverse("onlyProfits_app:account", kwargs={"username": "test_user"}))
        expected_saved_markets = self.client.get(reverse("onlyProfits_app:saved_markets", kwargs={"username": "test_user"}))
        self.assertTrue("user" in response.context)
        self.assertEqual(response.context["user"].saved_markets, expected_saved_markets)


class MarketsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            Market.objects.create(ticker="EXAMPLE" + str(i), values=[i, i + 3, i + 2, i + 4, i + 5], volume=66666)
    
    def test_check_template(self):
        self.assertTemplateUsed(self.client.get("onlyProfits:/markets"), "onlyProfits_app/markets.html")
    
    def test_context_dictionary(self):
        response = self.client.get(reverse("onlyProfits_app:markets"))
        expected_markets_order = Market.objects.order_by("volume")
        self.assertEqual(response.context["markets"], expected_markets_order)        


class SavedMarketsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(3):
            Market.objects.create(ticker="EXAMPLE" + str(i), values=[i, i + 3, i + 2, i + 4, i + 5], volume=66666)
        test_user = User.objects.create_user(username="test_user", password="test_password")
        OnlyProfitsUser.objects.create(django_user=test_user, saved_markets=json.dumps(["EXAMPLE1", "EXAMPLE2"]))
    
    def test_check_template(self):
        self.assertTemplateUsed(self.client.get("onlyProfits:/test_user/saved_markets"), "onlyProfits_app/saved_markets.html")
    
    def test_context_dictionary(self):
        response = self.client.get(reverse("onlyProfits_app:saved_markets", kwargs={"username": "test_user"}))
        expected_saved_markets = OnlyProfitsUser.objects.get(django_user=User.objects.get(username="test_user")).saved_markets
        # TODO parse json to arr
        arr = json.loads(expected_saved_markets)
        print("arr:", arr)
        self.assertEqual(response.context["saved_markets"], arr)


class SpecficMarketViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Market.objects.create(ticker="EXAMPLE1", values=[2, 3, 1, 6, 10], volume=66666)
    
    def test_check_template(self):
        self.assertTemplateUsed(self.client.get("onlyProfits:/market/EXAMPLE1"), "onlyProfits_app/market.html")
    
    def test_context_dictionary(self):
        response = self.client.get(reverse("onlyProfits_app:market", kwargs={"ticker": "EXAMPLE1"}))
        self.assertTrue("market" in response.context)
        self.assertEqual(response.context["market"], Market.objects.get(ticker="EXAMPLE1"))
