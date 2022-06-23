from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('koszyk', views.bucket),
    path('onas', views.about),
    path('restauracje', views.restaurants),
    path('menu', views.menu),
    path('kontakty', views.contact),
    path('api/jedzenie', views.endpoint_Food),
    path('api/jedzenie/<int:id>', views.apitest),
    path('api/restauracje', views.endpoint_Restaurant),
    path('dodajdokoszyka/<int:id>', views.addtobucket),
    path('daneklienta', views.inputData, name='dane'),
]