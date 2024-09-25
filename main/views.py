from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def handle_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'home/home.html')


def handle_contacts(request: HttpRequest) -> HttpResponse:
    return render(request, 'contacts/index.html')


def handle_about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about/index.html')
