from django.shortcuts import render

def index(request):
    return render(request, "utrrsApp/index.html")
