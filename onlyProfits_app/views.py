from django.shortcuts import render
from django.views import View

from onlyProfits_app.models import Market


class IndexView(View):
    def get(self, request):
        context_dict = {"markets": Market.objects.order_by("volume")[:5]}
        return render(request, "onlyProfits_app/onlyProfits.html", context_dict)


class AccountView(View):
    def get(self, request, username):
        context_dict = {"username": username}
        return render(request, "onlyProfits_app/account.html", context_dict)


class CreateAccountView(View):
    def get(self, request):
        return render(request, "onlyProfits_app/create_account.html")


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
