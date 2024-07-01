from django.shortcuts import render, redirect
# Вызываем готовую форму для логина
from django.contrib.auth.forms import AuthenticationForm
# Вызываем готовую функции для регистрации, логин и выход из системы
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.POST.get('next', '/'))

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

