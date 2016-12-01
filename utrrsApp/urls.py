from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),


    url(r'^about/$', views.about, name='about'),


    url(r'^history/$', views.history, name='history'),


    url(r'^roadmap/$', views.roadmap, name='roadmap'),

    url(r'^checkfont/$', views.checkfont, name='checkfont'),


    url(r'^assamese/$', views.assamese, name='assamese'),
    url(r'^assamese/codepoint$', views.assamese_codepoint, name='assamese_codepoint'),
    url(r'^assamese/gsub$', views.assamese_gsub, name='assamese_gsub'),
    url(r'^assamese/gpos$', views.assamese_gpos, name='assamese_gpos'),
    url(r'^assamese/report.pdf$', views.assamese_pdf, name='assamese_pdf'),
    url(r'^assamese/report.csv$', views.assamese_csv, name='assamese_csv'),
    url(r'^assamese/report.txt$', views.assamese_txt, name='assamese_txt'),


    url(r'^bengali/$', views.bengali, name='bengali'),
    url(r'^bengali/codepoint$', views.bengali_codepoint, name='bengali_codepoint'),
    url(r'^bengali/gsub$', views.bengali_gsub, name='bengali_gsub'),
    url(r'^bengali/gpos$', views.bengali_gpos, name='bengali_gpos'),
    url(r'^bengali/report.pdf$', views.bengali_pdf, name='bengali_pdf'),
    url(r'^bengali/report.csv$', views.bengali_csv, name='bengali_csv'),
    url(r'^bengali/report.txt$', views.bengali_txt, name='bengali_txt'),


    url(r'^german/$', views.german, name='german'),
    url(r'^german/codepoint$', views.german_codepoint, name='german_codepoint'),
    url(r'^german/gsub$', views.german_gsub, name='german_gsub'),
    url(r'^german/gpos$', views.german_gpos, name='german_gpos'),
    url(r'^german/report.pdf$', views.german_pdf, name='german_pdf'),
    url(r'^german/report.csv$', views.german_csv, name='german_csv'),
    url(r'^german/report.txt$', views.german_txt, name='german_txt'),


    url(r'^gujarati/$', views.gujarati, name='gujarati'),
    url(r'^gujarati/codepoint$', views.gujarati_codepoint, name='gujarati_codepoint'),
    url(r'^gujarati/gsub$', views.gujarati_gsub, name='gujarati_gsub'),
    url(r'^gujarati/gpos$', views.gujarati_gpos, name='gujarati_gpos'),
    url(r'^gujarati/report.pdf$', views.gujarati_pdf, name='gujarati_pdf'),
    url(r'^gujarati/report.csv$', views.gujarati_csv, name='gujarati_csv'),
    url(r'^gujarati/report.txt$', views.gujarati_txt, name='gujarati_txt'),


    url(r'^hindi/$', views.hindi, name='hindi'),
    url(r'^hindi/codepoint$', views.hindi_codepoint, name='hindi_codepoint'),
    url(r'^hindi/gsub$', views.hindi_gsub, name='hindi_gsub'),
    url(r'^hindi/gpos$', views.hindi_gpos, name='hindi_gpos'),
    url(r'^hindi/report.pdf$', views.hindi_pdf, name='hindi_pdf'),
    url(r'^hindi/report.csv$', views.hindi_csv, name='hindi_csv'),
    url(r'^hindi/report.txt$', views.hindi_txt, name='hindi_txt'),


    url(r'^kannada/$', views.kannada, name='kannada'),
    url(r'^kannada/codepoint$', views.kannada_codepoint, name='kannada_codepoint'),
    url(r'^kannada/gsub$', views.kannada_gsub, name='kannada_gsub'),
    url(r'^kannada/gpos$', views.kannada_gpos, name='kannada_gpos'),
    url(r'^kannada/report.pdf$', views.kannada_pdf, name='kannada_pdf'),
    url(r'^kannada/report.csv$', views.kannada_csv, name='kannada_csv'),
    url(r'^kannada/report.txt$', views.kannada_txt, name='kannada_txt'),


    url(r'^maithili/$', views.maithili, name='maithili'),
    url(r'^maithili/codepoint$', views.maithili_codepoint, name='maithili_codepoint'),
    url(r'^maithili/gsub$', views.maithili_gsub, name='maithili_gsub'),
    url(r'^maithili/gpos$', views.maithili_gpos, name='maithili_gpos'),
    url(r'^maithili/report.pdf$', views.maithili_pdf, name='maithili_pdf'),
    url(r'^maithili/report.csv$', views.maithili_csv, name='maithili_csv'),
    url(r'^maithili/report.txt$', views.maithili_txt, name='maithili_txt'),


    url(r'^malayalam/$', views.malayalam, name='malayalam'),
    url(r'^malayalam/codepoint$', views.malayalam_codepoint, name='malayalam_codepoint'),
    url(r'^malayalam/gsub$', views.malayalam_gsub, name='malayalam_gsub'),
    url(r'^malayalam/gpos$', views.malayalam_gpos, name='malayalam_gpos'),
     url(r'^malayalam/report.pdf$', views.malayalam_pdf, name='malayalam_pdf'),
    url(r'^malayalam/report.csv$', views.malayalam_csv, name='malayalam_csv'),
    url(r'^malayalam/report.txt$', views.malayalam_txt, name='malayalam_txt'),


    url(r'^marathi/$', views.marathi, name='marathi'),
    url(r'^marathi/codepoint$', views.marathi_codepoint, name='marathi_codepoint'),
    url(r'^marathi/gsub$', views.marathi_gsub, name='marathi_gsub'),
    url(r'^marathi/gpos$', views.marathi_gpos, name='marathi_gpos'),
    url(r'^marathi/report.pdf$', views.marathi_pdf, name='marathi_pdf'),
    url(r'^marathi/report.csv$', views.marathi_csv, name='marathi_csv'),
    url(r'^marathi/report.txt$', views.marathi_txt, name='marathi_txt'),


    url(r'^odia/$', views.odia, name='odia'),
    url(r'^odia/codepoint$', views.odia_codepoint, name='odia_codepoint'),
    url(r'^odia/gsub$', views.odia_gsub, name='odia_gsub'),
    url(r'^odia/gpos$', views.odia_gpos, name='odia_gpos'),
    url(r'^odia/report.pdf$', views.odia_pdf, name='odia_pdf'),
    url(r'^odia/report.csv$', views.odia_csv, name='odia_csv'),
    url(r'^odia/report.txt$', views.odia_txt, name='odia_txt'),


    url(r'^punjabi/$', views.punjabi, name='punjabi'),
    url(r'^punjabi/codepoint$', views.punjabi_codepoint, name='punjabi_codepoint'),
    url(r'^punjabi/gsub$', views.punjabi_gsub, name='punjabi_gsub'),
    url(r'^punjabi/gpos$', views.punjabi_gpos, name='punjabi_gpos'),
    url(r'^punjabi/report.pdf$', views.punjabi_pdf, name='punjabi_pdf'),
    url(r'^punjabi/report.csv$', views.punjabi_csv, name='punjabi_csv'),
    url(r'^punjabi/report.txt$', views.punjabi_txt, name='punjabi_txt'),


    url(r'^tamil/$', views.tamil, name='tamil'),
    url(r'^tamil/codepoint$', views.tamil_codepoint, name='tamil_codepoint'),
    url(r'^tamil/gsub$', views.tamil_gsub, name='tamil_gsub'),
    url(r'^tamil/gpos$', views.tamil_gpos, name='tamil_gpos'),
    url(r'^tamil/report.pdf$', views.tamil_pdf, name='tamil_pdf'),
    url(r'^tamil/report.csv$', views.tamil_csv, name='tamil_csv'),
    url(r'^tamil/report.txt$', views.tamil_txt, name='tamil_txt'),


    url(r'^telugu/$', views.telugu, name='telugu'),
    url(r'^telugu/codepoint$', views.telugu_codepoint, name='telugu_codepoint'),
    url(r'^telugu/gsub$', views.telugu_gsub, name='telugu_gsub'),
    url(r'^telugu/gpos$', views.telugu_gpos, name='telugu_gpos'),
    url(r'^telugu/report.pdf$', views.telugu_pdf, name='telugu_pdf'),
    url(r'^telugu/report.csv$', views.telugu_csv, name='telugu_csv'),
    url(r'^telugu/report.txt$', views.telugu_txt, name='telugu_txt'),
]