import json

from django.shortcuts import render
from django.views import View

from onlyProfits_app.models import Market



def GenerateMarkets():
    for i in ['BTCUSD', 'ETHUSD', 'MOIUSD', 'GUSUSD', 'WALTUSD']:
        values = []
        for j in range(10080):
            values.append(j)
        Market.objects.create(ticker=i, values=json.dumps(values), volume=20000)

class IndexView(View):
    def get(self, request):
        # GenerateMarkets()
        context_dict = {"markets": Market.objects.order_by("volume")[:5]}
        return render(request, "onlyProfits_app/index.html", context_dict)


class AccountView(View):
    def get(self, request, username):
        context_dict = {"user": username}
        return render(request, "onlyProfits_app/account.html", context_dict)


class CreateAccountView(View):
    def get(self, request):
        return render(request, "onlyProfits_app/create_account.html", {})


class MarketsView(View):
    def get(self, request):
        context_dict = {"markets": Market.objects.order_by("volume")}
        return render(request, "onlyProfits_app/markets.html", context_dict)


class SavedMarketsView(View):
    def get(self, request, username):
        context_dict = {"username": username}
        return render(request, "onlyProfits_app/saved_markets.html", context_dict)


class SpecificMarketView(View):
    def get(self, request, ticker):
        context_dict = {"ticker": ticker}
        return render(request, "onlyProfits_app/market.html", context_dict)