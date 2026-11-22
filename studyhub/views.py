from django.shortcuts import render
from django.http import FileResponse
from pathlib import Path
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

SOLAR_SYSTEM_PAGE = Path(__file__).resolve().parent.parent / "solar_system.html"


def home(request):
    return render(request, "studyhub/home.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "studyhub/signup.html", {"form": form})


def science(request):
    return render(request, "studyhub/science.html")


def django_guide(request):
    return render(request, "studyhub/django_guide.html")


def solar_system(request):
    return FileResponse(SOLAR_SYSTEM_PAGE.open("rb"), content_type="text/html")
