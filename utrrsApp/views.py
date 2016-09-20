from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def history(request):
	return render(request, 'history.html')

def roadmap(request):
	return render(request, 'roadmap.html')

def hindi(request):
	return render(request, 'hindi.html')

