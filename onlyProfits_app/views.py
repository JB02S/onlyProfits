from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, "onlyProfits_app/onlyProfits.html")


class AccountView(View):
    def get(self, request, username):
        return render(request, "onlyProfits_app/account.html", {})


class CreateAccountView(View):
    def get(self, request):
        return render(request, "onlyProfits_app/create_account.html")


class MarketsView(View):
    def get(self, request):
        return render(request, "onlyProfits_app/markets.html")


class SavedMarketsView(View):
    def get(self, request, username):
        return render(request, "onlyProfits_app/saved_markets.html", {})


class SpecificMarketView(View):
    def get(self, request, ticker):
        return render(request, "onlyProfits_app/market.html", {})
