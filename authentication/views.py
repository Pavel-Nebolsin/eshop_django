from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response


class MyLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context


def logout_view(request):
    logout(request)
    return redirect('index')
