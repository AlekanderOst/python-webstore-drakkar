from django.urls import path
from . import views as cartViews




urlpatterns = [
    path('/cart/<str:username>',cartViews.CartView.as_view(), name='cart'),
    path('/cart/<str:pk>/delete',cartViews.DeleteProduct.as_view(), name='del'),
]