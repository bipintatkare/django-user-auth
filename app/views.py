from django.shortcuts import render, redirect
from .models import User


def auth(request):
    return render(request, "auth.html")


def register(request):

    try:
        if request.method == "POST":

            first_name = request.POST.get("first-name", "")
            last_name = request.POST.get("last-name", "")
            email = request.POST.get("email", "")
            address = request.POST.get("address", "")
            contact = request.POST.get("contact", "")
            password = request.POST.get("password", "")

            User.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password,
                contact = contact,
                address = address
            )

            print(f"User {first_name} registered successfully")

    except Exception as ep:

        print(f"{ep=}")

    return redirect('auth')


def login(request):

    try:

        if request.method == "POST":

            email = request.POST.get("email", "")
            password = request.POST.get("password", "")

            User.objects.get(email=email, password=password)

            print("login successful")

    except Exception as ep:

        print(f"{ep=}")

    return redirect('auth')