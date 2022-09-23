from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'onlyProfits_app/onlyProfits.html')


class AccountView(View):
    pass


class CreateAccountView(View):
    pass


class MarketsView(View):
    pass


class SavedMarketsView(View):
    pass


class SpecificMarketView(View):
    pass
