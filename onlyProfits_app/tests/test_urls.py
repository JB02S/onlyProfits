from django.test import SimpleTestCase
from django.urls import reverse, resolve
from onlyProfits_app.views import AccountView, CreateAccountView, IndexView, MarketsView, SavedMarketsView, SpecificMarketView
from onlyProfits_app.models import Market
from django.contrib.auth.models import User

"""
Using SimpleTestCase rather than TestCase as do not need to interact with database
"""

class TestUrls(SimpleTestCase):
    
    def test_index_url_resolves(self):
        url = reverse('onlyProfits_app:index')
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_create_account_url_resolves(self):
        url = reverse('onlyProfits_app:create_account')
        self.assertEquals(resolve(url).func.view_class, CreateAccountView)
    
    def test_account_url_resolves(self):
        account = User.objects.create()
        url = reverse('onlyProfits_app:account', kwargs=account.username)
        self.assertEquals(resolve(url).func.view_class, AccountView)

    def test_markets_url_resolves(self):
        url = reverse('onlyProfits_app:markets')
        self.assertEquals(resolve(url).func.view_class, MarketsView)

    def test_saved_markets_url_resolves(self):
        account = User.objects.create()
        url = reverse('onlyProfits_app:saved_markets', kwargs=account.username)
        self.assertEquals(resolve(url).func.view_class, SavedMarketsView)

    def test_specific_market_url_resolves(self):
        market = Market.objects.create()
        url = reverse('onlyProfits_app:specific_market', kwargs=market.ticker)
        self.assertEquals(resolve(url).func.view_class, SpecificMarketView)
    
