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

def assamese(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/codepoint/master_as_IN.txt')
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
	return render(request, 'assamese.html', {'data': data[1:]})

def bengali(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/data/codepoint/master_bn_IN.txt')
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
	return render(request, 'bengali.html', {'data': data[1:]})

def german(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/de_DE/font/data/codepoint/master_de_DE.txt')
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
	return render(request, 'german.html', {'data': data[1:]})

def gujarati(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/data/codepoint/master_gu_IN.txt')
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
	return render(request, 'gujarati.html', {'data': data[1:]})

def hindi(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/codepoint/master_hi_IN.txt')
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
	return render(request, 'hindi.html', {'data': data[1:]})

def kannada(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/data/codepoint/master_kn_IN.txt')
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
	return render(request, 'kannada.html', {'data': data[1:]})

def maithili(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/data/codepoint/master_mai_IN.txt')
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
	return render(request, 'maithili.html', {'data': data[1:]})

def malayalam(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/data/codepoint/master_ml_IN.txt')
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
	return render(request, 'malayalam.html', {'data': data[1:]})

def marathi(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/data/codepoint/master_mr_IN.txt')
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
	return render(request, 'marathi.html', {'data': data[1:]})

def odia(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/data/codepoint/master_or_IN.txt')
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
	return render(request, 'odia.html', {'data': data[1:]})

def punjabi(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/data/codepoint/master_pa_IN.txt')
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
	return render(request, 'punjabi.html', {'data': data[1:]})

def tamil(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/data/codepoint/master_te_IN.txt')
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
	return render(request, 'tamil.html', {'data': data[1:]})

def telugu(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/data/codepoint/master_te_IN.txt')
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
	return render(request, 'telugu.html', {'data': data[1:]})
