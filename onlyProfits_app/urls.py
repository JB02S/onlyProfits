from django.contrib import admin
from django.urls import path
from django.urls import include

from onlyProfits_app import views

app_name = 'onlyProfits_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
