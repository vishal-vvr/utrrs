from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def history(request):
	return render(request, 'history.html')

def roadmap(request):
	return render(request, 'roadmap.html')

def hindi(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/codepoint/master_hi.txt')
	file = open(file_path)
	c = file.read()
	length = c.count('\n')
	file.close()
	file = open(file_path)
	data = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data.append(sp)
	return render(request, 'test.html', {'data': data[1:]})
