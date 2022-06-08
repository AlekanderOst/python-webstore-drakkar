
from .models import Good
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from cart.forms import CartForm

from django.urls import reverse


def new_home(request):
    data = {'title': 'main',
            'body': 'main'
            }
    return render(request, 'goods/new-home.html', data)


def about(request):
    data = {'title': 'About',
            'body': 'about'
            }
    return render(request, 'goods/about.html', data)


def contact(request):
    data = {'title': 'contact',
            'body': 'contact'
            }
    return render(request, 'goods/contact.html', data)


class All(ListView):
    model = Good
    template_name = 'goods/all-goods.html'
    context_object_name = 'goods'
    ordering = ['id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(All, self).get_context_data(**kwargs)
        ctx['title'] = 'Main'
        return ctx


class Backpacks(ListView):
    model = Good
    template_name = 'goods/backpacks.html'
    context_object_name = 'goods'
    ordering = ['id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Backpacks, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная'
        return ctx


class Bags(ListView):
    model = Good
    template_name = 'goods/bags.html'
    context_object_name = 'goods'
    ordering = ['id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Bags, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная'
        return ctx


class Wallets(ListView):
    model = Good
    template_name = 'goods/wallets.html'
    context_object_name = 'goods'
    ordering = ['id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Wallets, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная'
        return ctx


class Accessories(ListView):
    model = Good
    template_name = 'goods/accessories.html'
    context_object_name = 'goods'
    ordering = ['id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Accessories, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная'
        return ctx


class GoodDetailPage(DetailView, CreateView):
    objects = None
    model = Good
    form_class = CartForm
    template_name = 'goods/good-detail.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.slug = None

    def form_valid(self, form_class,**kwargs):
        form_class.instance.author = self.request.user
        form_class.instance.img = super(GoodDetailPage, self).get_object().img
        form_class.instance.title = super(GoodDetailPage, self).get_object()
        return super().form_valid(form_class)

    def get_absolute_url(self):
        return reverse('good-detail', kwargs={'slug': self.slug})
