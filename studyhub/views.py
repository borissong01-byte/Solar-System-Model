from django.shortcuts import render
from django.http import FileResponse
from pathlib import Path

SOLAR_SYSTEM_PAGE = Path(__file__).resolve().parent.parent / "solar_system.html"


def home(request):
    return render(request, "studyhub/home.html")


def science(request):
    return render(request, "studyhub/science.html")


def solar_system(request):
    return FileResponse(SOLAR_SYSTEM_PAGE.open("rb"), content_type="text/html")
