from django.shortcuts import render
from .forms import LoginForm, EditAccountForm, RegistrationForm
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, "authentication/index.html")


def login(request):
    form = LoginForm(data=request.POST)
    title = "Login"

    if request.method == "POST" and form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("catalog"))

    context = {
        "title": title,
        "form": form,
    }
    return render(request, "authentication/login.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("catalog"))


def registration(request):
    title = "Registration"
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("catalog"))
    else:
        form = RegistrationForm()
    context = {
        "title": title,
        "form": form
    }
    return render(request, "authentication/register.html", context)


def edit_account(request):
    title = "Edit account"
    if request.method == "POST":
        form = EditAccountForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = EditAccountForm(instance=request.user)
    context = {
        "title": title,
        "form": form
    }
    return render(request, "authentication/edit_account.html", context)
