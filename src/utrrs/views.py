from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse("Home page")
    return render(request, "utrrsApp/utrrs_website/home.html")

def about(request):
    return render(request, "utrrsApp/utrrs_website/about.html")

def checkfont(request):
    return render(request, "utrrsApp/utrrs_website/checkfont.html")
