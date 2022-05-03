from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} has been successfully created')
            return redirect('all-goods')
    else:
        form = UserRegisterForm()
    return render(
        request,
        'users/registration.html',
        {'title': 'Registration page',
         'form': form,
         })