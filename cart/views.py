from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DeleteView
from cart.models import Cart


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








