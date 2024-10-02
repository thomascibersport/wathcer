from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
import requests


def handle_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'home/home.html')


def handle_contacts(request: HttpRequest) -> HttpResponse:
    return render(request, 'contacts/index.html')

FASTAPI_UPLOAD_URL = "http://127.0.0.1:8000/files/upload"

def handle_about(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        if request.method == 'POST':
            uploaded_file = request.FILES['file']  # Retrieve the file from the request

            # Make a POST request to the FastAPI server with the file
            with uploaded_file.open('rb') as file_content:
                response = requests.post(
                    FASTAPI_UPLOAD_URL,
                    files={"file": (uploaded_file.name, file_content, uploaded_file.content_type)}
                )

            # Handle the response from FastAPI
            if response.status_code == 200:
                return redirect('/about/')
            else:
                return HttpResponse(f"Failed to upload file. Response: {response.content}", status=response.status_code)

    response = requests.get("http://127.0.0.1:8000/files")
    data = response.json()

    return render(request, 'about/index.html', {'files': data})
