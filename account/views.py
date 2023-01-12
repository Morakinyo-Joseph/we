from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def landing_page(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("core:dashboard")
        return redirect("market:homepage")
   

    return render(request, 'landing_page.html')


def log_in(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("core:dashboard")
        return redirect("market:homepage")

    # main code
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        the_user = authenticate(username=username, password=password)

        if the_user is not None:
            login(request, the_user)

            messages.success(request, "Login successful")

            if request.user.is_staff:
                return redirect("core:dashboard")

            return redirect("market:homepage")
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, "account/login.html")


def log_out(request):
    logout(request)

    messages.success(request, "Logout successful")
    return redirect("account:login")