from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from random import randint
from django.shortcuts import render

from app_one.forms import RegisterForm

# Create your views here.


class IndexView(TemplateView):
    template_name = 'app_one/index.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'app_one/register.html'
    success_url = reverse_lazy('app_one:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>This username already exists</div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>This username is available</div>")


def view_currency(request):
    return render(request, 'app_one/currency.html')


def get_currency(request):
    return render(request, 'app_one/partials/content.html', {"USD": randint(10, 100), "ERO": randint(10, 100), "BDT": randint(99, 200)})
