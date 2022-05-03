from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all-goods', views.All.as_view(), name='all-goods'),
    path('good/<slug>',views.GoodDetailPage.as_view(),name='good-detail'),
    path('',views.new_home, name='new-home.html'),
    path('about',views.about, name='about.html'),
    path('backpacks', views.Backpacks.as_view(), name='backpacks'),
    path('bags', views.Bags.as_view(), name='bags'),
    path('wallets', views.Wallets.as_view(), name='wallets'),
    path('accessories', views.Accessories.as_view(), name='accessories'),
    path('contact', views.contact, name='contact'),
]
