from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "title":"News"
    }
    return render(request, "blog/index.html", context)




