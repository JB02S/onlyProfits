from django.test import SimpleTestCase
from django.urls import reverse, resolve
from onlyProfits_app.views import IndexView

"""
Using SimpleTestCase rather than TestCase as do not need to interact with database
"""


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('onlyProfits_app:index')
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_account_url_resolves(self):
        pass

    def test_markets_url_resolves(self):
        pass

    def test_create_new_account_url_resolves(self):
        pass

    def test_saved_markets_url_resolves(self):
        pass

    def test_specific_market_url_resolves(self):
        pass
