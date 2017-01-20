# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import os, filecmp, csv
import shlex, subprocess
from collections import Counter
from django.http import JsonResponse
from wsgiref.util import FileWrapper
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from terminaltables import AsciiTable
from itertools import izip
from PIL import Image

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def history(request):
	return render(request, 'history.html')

def roadmap(request):
	return render(request, 'roadmap.html')

def checkfont(request):
	return render(request, 'check_font.html')

def assamese(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/master_as.txt')
			img_path = os.path.join(module_dir, 'static/lang/as_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-assamese/Lohit-Assamese.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/as_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/as_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-assamese',font_path))
			doc = SimpleDocTemplate("assamese-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-assamese'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('assamese-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('assamese-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'assamese.html')
	else:
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
		return render(request, 'assamese.html', {'data_code': data_code})

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

def assamese_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/assamese-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=assamese-report.pdf'
	file.close()
	return response

def assamese_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/assamese-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=assamese-report.csv'
	file.close()
	return response

def assamese_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/assamese-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=assamese-report.txt'
	file.close()
	return response

def bengali(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/data/master_bn.txt')
			img_path = os.path.join(module_dir, 'static/lang/bn_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-bengali/Lohit-Bengali.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/bn_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/bn_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-bengali',font_path))
			doc = SimpleDocTemplate("bengali-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-bengali'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('bengali-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('bengali-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'bengali.html')
	else:
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
		return render(request, 'bengali.html', {'data_code': data_code})

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

def bengali_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/bengali-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=bengali-report.pdf'
	file.close()
	return response

def bengali_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/bengali-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=bengali-report.csv'
	file.close()
	return response

def bengali_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/bengali-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=bengali-report.txt'
	file.close()
	return response

def german(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/de_DE/font/data/codepoint/master_de_DE.txt')
			img_path = os.path.join(module_dir, 'static/lang/de_DE/font/')
			font_path = os.path.join(module_dir, 'static/fonts/dejavu/DejaVuSans.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/de_DE/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/de_DE/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('dejavu',font_path))
			doc = SimpleDocTemplate("german-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'dejavu'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('german-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('german-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'german.html')
	else:
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
		return render(request, 'german.html', {'data_code': data_code})

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
	return render(request, 'de_codepoint.html', {'data_code': data_code})

def german_gsub(request):
	return render(request, 'de_gsub.html')

def german_gpos(request):
	return render(request, 'de_gpos.html')

def german_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/de_DE/font/german-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=german-report.pdf'
	file.close()
	return response

def german_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/de_DE/font/german-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=german-report.csv'
	file.close()
	return response

def german_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/de_DE/font/german-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=german-report.txt'
	file.close()
	return response

def gujarati(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/data/master_gu.txt')
			img_path = os.path.join(module_dir, 'static/lang/gu_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-gujarati/Lohit-Gujarati.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/gu_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/gu_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-gujarati',font_path))
			doc = SimpleDocTemplate("gujarati-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-gujarati'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('gujarati-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('gujarati-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'gujarati.html')
	else:
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
		return render(request, 'gujarati.html', {'data_code': data_code})

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

def gujarati_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/gujarati-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=gujarati-report.pdf'
	file.close()
	return response

def gujarati_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/gujarati-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=gujarati-report.csv'
	file.close()
	return response

def gujarati_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/gujarati-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=gujarati-report.txt'
	file.close()
	return response

def hindi(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/master_hi.txt')
			img_path = os.path.join(module_dir, 'static/lang/hi_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-devanagari/Lohit-Devanagari.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/hi_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/hi_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-devanagari',font_path))
			doc = SimpleDocTemplate("hindi-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-devanagari'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('hindi-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('hindi-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'hindi.html')
	else:
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
		return render(request, 'hindi.html', {'data_code': data_code})

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

def hindi_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/hindi-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=hindi-report.pdf'
	file.close()
	return response

def hindi_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/hindi-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=hindi-report.csv'
	file.close()
	return response

def hindi_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/hindi-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=hindi-report.txt'
	file.close()
	return response

def kannada(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/data/master_kn.txt')
			img_path = os.path.join(module_dir, 'static/lang/kn_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-kannada/Lohit-Kannada.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/kn_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/kn_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-kannada',font_path))
			doc = SimpleDocTemplate("kannada-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-kannada'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('kannada-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('kannada-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'kannada.html')
	else:
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
		return render(request, 'kannada.html', {'data_code': data_code})

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

def kannada_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/kannada-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=kannada-report.pdf'
	file.close()
	return response

def kannada_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/kannada-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=kannada-report.csv'
	file.close()
	return response

def kannada_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/kannada-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=kannada-report.txt'
	file.close()
	return response

def maithili(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/data/master_mai.txt')
			img_path = os.path.join(module_dir, 'static/lang/mai_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-devanagari/Lohit-Devanagari.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/mai_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/mai_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-devanagari',font_path))
			doc = SimpleDocTemplate("maithili-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-devanagari'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('maithili-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('maithili-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'maithili.html')
	else:
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
		return render(request, 'maithili.html', {'data_code': data_code})

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

def maithili_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/maithili-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=maithili-report.pdf'
	file.close()
	return response

def maithili_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/maithili-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=maithili-report.csv'
	file.close()
	return response

def maithili_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/maithili-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=maithili-report.txt'
	file.close()
	return response

def malayalam(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/data/master_ml.txt')
			img_path = os.path.join(module_dir, 'static/lang/ml_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/smc/Meera.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/ml_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/ml_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('smc',font_path))
			doc = SimpleDocTemplate("malayalam-report.pdf", pagesize=A4, rightMargin=0,leftMargin=0, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'smc'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('malayalam-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('malayalam-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'malayalam.html')
	else:
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
		return render(request, 'malayalam.html', {'data_code': data_code})

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

def malayalam_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/malayalam-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=malayalam-report.pdf'
	file.close()
	return response

def malayalam_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/malayalam-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=malayalam-report.csv'
	file.close()
	return response

def malayalam_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/malayalam-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=malayalam-report.txt'
	file.close()
	return response

def marathi(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/data/master_mr.txt')
			img_path = os.path.join(module_dir, 'static/lang/mr_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-devanagari/Lohit-Devanagari.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/mr_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/mr_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-devanagari',font_path))
			doc = SimpleDocTemplate("marathi-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-devanagari'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('marathi-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('marathi-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'marathi.html')
	else:
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
		return render(request, 'marathi.html', {'data_code': data_code})

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

def marathi_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/marathi-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=marathi-report.pdf'
	file.close()
	return response

def marathi_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/marathi-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=marathi-report.csv'
	file.close()
	return response

def marathi_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/marathi-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=marathi-report.txt'
	file.close()
	return response

def odia(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/or_IN/font/data/master_or.txt')
			img_path = os.path.join(module_dir, 'static/lang/or_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-odia/Lohit-Odia.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/or_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/or_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-odia',font_path))
			doc = SimpleDocTemplate("odia-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-odia'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('odia-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('odia-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'odia.html')
	else:
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
		return render(request, 'odia.html', {'data_code': data_code})

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

def odia_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/odia-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=odia-report.pdf'
	file.close()
	return response

def odia_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/odia-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=odia-report.csv'
	file.close()
	return response

def odia_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/odia-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=odia-report.txt'
	file.close()
	return response

def punjabi(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/data/master_pa.txt')
			img_path = os.path.join(module_dir, 'static/lang/pa_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-gurmukhi/Lohit-Gurmukhi.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/pa_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/pa_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-gurmukhi',font_path))
			doc = SimpleDocTemplate("punjabi-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-gurmukhi'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('punjabi-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('punjabi-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'punjabi.html')
	else:
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
		return render(request, 'punjabi.html', {'data_code': data_code})

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

def punjabi_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/punjabi-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=punjabi-report.pdf'
	file.close()
	return response

def punjabi_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/punjabi-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=punjabi-report.csv'
	file.close()
	return response

def punjabi_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/punjabi-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=punjabi-report.txt'
	file.close()
	return response

def tamil(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/data/master_ta.txt')
			img_path = os.path.join(module_dir, 'static/lang/ta_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-tamil/Lohit-Tamil.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/ta_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/ta_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-tamil',font_path))
			doc = SimpleDocTemplate("tamil-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-tamil'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('tamil-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('tamil-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'tamil.html')
	else:
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
		return render(request, 'tamil.html', {'data_code': data_code})

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

def tamil_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/tamil-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=tamil-report.pdf'
	file.close()
	return response

def tamil_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/tamil-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=tamil-report.csv'
	file.close()
	return response

def tamil_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/tamil-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=tamil-report.txt'
	file.close()
	return response

def telugu(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/te_IN/font/data/master_te.txt')
			img_path = os.path.join(module_dir, 'static/lang/te_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-telugu/Lohit-Telugu.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/te_IN/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/te_IN/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('lohit-telugu',font_path))
			doc = SimpleDocTemplate("telugu-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'lohit-telugu'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('telugu-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('telugu-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'telugu.html')
	else:
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
		return render(request, 'telugu.html', {'data_code': data_code})

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

def telugu_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/telugu-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=telugu-report.pdf'
	file.close()
	return response

def telugu_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/telugu-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=telugu-report.csv'
	file.close()
	return response

def telugu_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/telugu-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=telugu-report.txt'
	file.close()
	return response

def japanese(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/ja_JP/font/data/master_ja.txt')
			img_path = os.path.join(module_dir, 'static/lang/ja_JP/font/')
			font_path = os.path.join(module_dir, 'static/fonts/vlgothic/VL-Gothic-Regular.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			pdf_data = [['Codepoint','Character','Description','Matched %','Result']]
			os.chdir(img_path)
			match_count = 0
			unmatch_count = 0
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=png --output-file=%s.png' % (font_path, sp[2], name))
				or_name = sp[1].strip('.svg')
				img1 = os.path.join(module_dir, 'static/lang/ja_JP/font/%s.png' % or_name)
				img2 = os.path.join(module_dir, 'static/lang/ja_JP/font/%s.png' % name)
				i1 = Image.open(img1)
				i2 = Image.open(img2)
				pairs = izip(i1.getdata(), i2.getdata())
				if len(i1.getbands()) == 1:
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				ncomponents = i1.size[0] * i1.size[1] * 3
				diff = (dif / 255.0 * 100) / ncomponents
				mat = float(100-diff)
				per = "%s %%" % round(mat,2)
				sp.append(per)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
					match_count += 1
				else:
					sp.append('Not Matched')
					unmatch_count += 1
				pd = sp[:]
				pd.pop(1)
				pdf_data.append(pd)
				data_code.append(sp)
				os.remove('%s.png' % name)
			"""PDF Generating"""
			pdfmetrics.registerFont(TTFont('vlgothic',font_path))
			doc = SimpleDocTemplate("japanese-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
			elements = []
			table = Table(pdf_data)
			table.setStyle(TableStyle([
			    ('FONT', (1, 0), (1, -1), 'vlgothic'),
			    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			    ('FONTSIZE', (0, 0), (-1, -1), 8),
			    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
			    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			]))
			styles = getSampleStyleSheet()
			p = Paragraph("<u>Report</u>\n", styles["title"])
			elements.append(p)
			elements.append(table)
			doc.build(elements)
			"""Libre Office Generating"""
			with open('japanese-report.csv', 'w') as csvfile:
				writer = csv.writer(csvfile)
				[writer.writerow(r) for r in pdf_data]
			"""Text File Generating"""
			table_instance = AsciiTable(pdf_data, 'Report')
			table_instance.justify_columns[1] = 'left'
			table_instance.inner_row_border = True
			with open('japanese-report.txt','w') as f:
				f.write(table_instance.table)
    		return JsonResponse({'data_code': data_code, 'match_count': match_count, 'unmatch_count': unmatch_count})
		return render(request, 'japanese.html')
	else:
		module_dir = os.path.dirname(__file__)
		file_path = os.path.join(module_dir, 'static/lang/ja_JP/font/data/master_ja.txt')
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
		return render(request, 'japanese.html', {'data_code': data_code})

def japanese_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ja_JP/font/data/codepoint/master_ja_JP.txt')
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
	return render(request, 'ja_codepoint.html', {'data_code': data_code[1:]})

def japanese_gsub(request):
	return render(request, 'ja_gsub.html')

def japanese_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ja_JP/font/data/gpos/master_gpos_ja_JP.txt')
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
	return render(request, 'ja_gpos.html', {'data_gpos': data_gpos[1:]})

def japanese_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ja_JP/font/japanese-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=japanese-report.pdf'
	file.close()
	return response

def japanese_csv(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ja_JP/font/japanese-report.csv')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=japanese-report.csv'
	file.close()
	return response

def japanese_txt(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ja_JP/font/japanese-report.txt')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/text')
	response['Content-Disposition'] = 'attachment; filename=japanese-report.txt'
	file.close()
	return response

