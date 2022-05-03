from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
# Create your views here.
from cart.models import Cart
from goods.models import Good


class CartView(ListView):
    model = Cart
    context_object_name = 'cart'
    template_name = 'cart/cart.html'


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Cart.objects.filter(author=user)


class DeleteProduct(DeleteView):
    model = Cart
    template_name = 'cart/delete_product.html'
    success_url = '/all-goods'








