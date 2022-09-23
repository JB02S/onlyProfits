from django.contrib import admin
from django.urls import path
from django.urls import include

from onlyProfits_app import views

app_name = 'onlyProfits_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('account/<username>', views.AccountView.as_view(), name='account'),
    path('create_account/', views.CreateAccountView.as_view(), name='create_account'),
    path('markets/', views.MarketsView.as_view(), name='markets'),
    path('market/<ticker>', views.SpecificMarketView.as_view(), name='specific_market'),
    path('account/<username>/saved_markets/', views.SavedMarketsView.as_view(), name='saved_markets'),
]
