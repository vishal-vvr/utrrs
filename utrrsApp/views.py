from django.shortcuts import render
from django.http import HttpResponse
import os
import shlex, subprocess
from collections import Counter

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
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/master_as.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'assamese.html', {'data_code': data_code[1:]})

def assamese_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/codepoint/master_as_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'as_codepoint.html', {'data_code': data_code[1:]})

def assamese_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/gsub/master_gsub_as_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'as_gsub.html', {'data_gsub': data_gsub[1:]})

def assamese_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/gpos/master_gpos_as_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'as_gpos.html', {'data_gpos': data_gpos[1:]})

def bengali(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/data/master_bn.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	module_dir = os.path.dirname(__file__)
	return render(request, 'bengali.html', {'data_code': data_code[1:]})

def bengali_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/data/codepoint/master_bn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'bn_codepoint.html', {'data_code': data_code[1:]})

def bengali_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/data/gsub/master_gsub_bn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'bn_gsub.html', {'data_gsub': data_gsub[1:]})

def bengali_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/data/gpos/master_gpos_bn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'bn_gpos.html', {'data_gpos': data_gpos[1:]})

def german(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/de_DE/font/data/codepoint/master_de_DE.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'german.html', {'data_code': data_code[1:]})

def german_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/de_DE/font/data/codepoint/master_de_DE.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'de_codepoint.html', {'data_code': data_code[1:]})

def german_gsub(request):
	return render(request, 'de_gsub.html')

def german_gpos(request):
	return render(request, 'de_gpos.html')

def gujarati(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/data/master_gu.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'gujarati.html', {'data_code': data_code[1:]})

def gujarati_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/data/codepoint/master_gu_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'gu_codepoint.html', {'data_code': data_code[1:]})

def gujarati_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/data/gsub/master_gsub_gu_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'gu_gsub.html', {'data_gsub': data_gsub[1:]})

def gujarati_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/data/gpos/master_gpos_gu_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'gu_gpos.html', {'data_gpos': data_gpos[1:]})

def hindi(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/master_hi.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'hindi.html', {'data_code': data_code[1:]})

def hindi_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/codepoint/master_hi_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'hi_codepoint.html', {'data_code': data_code[1:]})

def hindi_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/gsub/master_gsub_hi_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'hi_gsub.html', {'data_gsub': data_gsub[1:]})

def hindi_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/gpos/master_gpos_hi_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'hi_gpos.html', {'data_gpos': data_gpos[1:]})

def kannada(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/data/master_kn.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'kannada.html', {'data_code': data_code[1:]})

def kannada_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/data/codepoint/master_kn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'kn_codepoint.html', {'data_code': data_code[1:]})

def kannada_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/data/gsub/master_gsub_kn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'kn_gsub.html', {'data_gsub': data_gsub[1:]})

def kannada_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/data/gpos/master_gpos_kn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'kn_gpos.html', {'data_gpos': data_gpos[1:]})

def maithili(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/data/master_mai.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'maithili.html', {'data_code': data_code[1:]})

def maithili_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/data/codepoint/master_mai_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'mai_codepoint.html', {'data_code': data_code[1:]})

def maithili_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/data/gsub/master_gsub_mai_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'mai_gsub.html', {'data_gsub': data_gsub[1:]})

def maithili_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/data/gpos/master_gpos_mai_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'mai_gpos.html', {'data_gpos': data_gpos[1:]})

def malayalam(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/data/master_ml.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'malayalam.html', {'data_code': data_code[1:]})

def malayalam_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/data/codepoint/master_ml_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'ml_codepoint.html', {'data_code': data_code[1:]})

def malayalam_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/data/gsub/master_gsub_ml_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'ml_gsub.html', {'data_gsub': data_gsub[1:]})

def malayalam_gpos(request):
	return render(request, 'ml_gpos.html')

def marathi(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/data/master_mr.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'marathi.html', {'data_code': data_code[1:]})

def marathi_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/data/codepoint/master_mr_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'mr_codepoint.html', {'data_code': data_code[1:]})

def marathi_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/data/gsub/master_gsub_mr_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'mr_gsub.html', {'data_gsub': data_gsub[1:]})

def marathi_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/data/gpos/master_gpos_mr_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'mr_gpos.html', {'data_gpos': data_gpos[1:]})

def odia(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/data/master_or.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'odia.html', {'data_code': data_code[1:]})

def odia_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/data/codepoint/master_or_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'or_codepoint.html', {'data_code': data_code[1:]})

def odia_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/data/gsub/master_gsub_or_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'or_gsub.html', {'data_gsub': data_gsub[1:]})

def odia_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/data/gpos/master_gpos_or_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'or_gpos.html', {'data_gpos': data_gpos[1:]})

def punjabi(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/data/master_pa.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'punjabi.html', {'data_code': data_code[1:]})

def punjabi_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/data/codepoint/master_pa_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'pa_codepoint.html', {'data_code': data_code[1:]})

def punjabi_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/data/gsub/master_gsub_pa_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'pa_gsub.html', {'data_gsub': data_gsub[1:]})

def punjabi_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/data/gpos/master_gpos_pa_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'pa_gpos.html', {'data_gpos': data_gpos[1:]})

def tamil(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/data/master_ta.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'tamil.html', {'data_code': data_code[1:]})

def tamil_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/data/codepoint/master_ta_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'ta_codepoint.html', {'data_code': data_code[1:]})

def tamil_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/data/gsub/master_gsub_ta_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'ta_gsub.html', {'data_gsub': data_gsub[1:]})

def tamil_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/data/gpos/master_gpos_ta_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'ta_gpos.html', {'data_gpos': data_gpos[1:]})

def telugu(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/data/master_te.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'telugu.html', {'data_code': data_code[1:]})

def telugu_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/data/codepoint/master_te_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'te_codepoint.html', {'data_code': data_code[1:]})

def telugu_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/data/gsub/master_gsub_te_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'te_gsub.html', {'data_gsub': data_gsub[1:]})

def telugu_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/data/gpos/master_gpos_te_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'te_gpos.html', {'data_gpos': data_gpos[1:]})

def checkfont(request):
	"""command = 'fc-match sans-serif:lang=te'
	command = shlex.split(c)
	res = subprocess.check_output(x)
	Counter(z) == Counter(q)"""
	return render(request, 'check_font.html')

