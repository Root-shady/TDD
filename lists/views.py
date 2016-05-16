from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse("""<html><head><title>To-Do lists</title></head>
                    <body><h1>This is a to-do list</h1></body>
                    </html>""")
