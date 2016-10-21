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


    url(r'^bengali/$', views.bengali, name='bengali'),
    url(r'^bengali/codepoint$', views.bengali_codepoint, name='bengali_codepoint'),
    url(r'^bengali/gsub$', views.bengali_gsub, name='bengali_gsub'),
    url(r'^bengali/gpos$', views.bengali_gpos, name='bengali_gpos'),


    url(r'^german/$', views.german, name='german'),
    url(r'^german/codepoint$', views.german_codepoint, name='german_codepoint'),
    url(r'^german/gsub$', views.german_gsub, name='german_gsub'),
    url(r'^german/gpos$', views.german_gpos, name='german_gpos'),


    url(r'^gujarati/$', views.gujarati, name='gujarati'),
    url(r'^gujarati/codepoint$', views.gujarati_codepoint, name='gujarati_codepoint'),
    url(r'^gujarati/gsub$', views.gujarati_gsub, name='gujarati_gsub'),
    url(r'^gujarati/gpos$', views.gujarati_gpos, name='gujarati_gpos'),


    url(r'^hindi/$', views.hindi, name='hindi'),
    url(r'^hindi/codepoint$', views.hindi_codepoint, name='hindi_codepoint'),
    url(r'^hindi/gsub$', views.hindi_gsub, name='hindi_gsub'),
    url(r'^hindi/gpos$', views.hindi_gpos, name='hindi_gpos'),


    url(r'^kannada/$', views.kannada, name='kannada'),
    url(r'^kannada/codepoint$', views.kannada_codepoint, name='kannada_codepoint'),
    url(r'^kannada/gsub$', views.kannada_gsub, name='kannada_gsub'),
    url(r'^kannada/gpos$', views.kannada_gpos, name='kannada_gpos'),


    url(r'^maithili/$', views.maithili, name='maithili'),
    url(r'^maithili/codepoint$', views.maithili_codepoint, name='maithili_codepoint'),
    url(r'^maithili/gsub$', views.maithili_gsub, name='maithili_gsub'),
    url(r'^maithili/gpos$', views.maithili_gpos, name='maithili_gpos'),


    url(r'^malayalam/$', views.malayalam, name='malayalam'),
    url(r'^malayalam/codepoint$', views.malayalam_codepoint, name='malayalam_codepoint'),
    url(r'^malayalam/gsub$', views.malayalam_gsub, name='malayalam_gsub'),
    url(r'^malayalam/gpos$', views.malayalam_gpos, name='malayalam_gpos'),


    url(r'^marathi/$', views.marathi, name='marathi'),
    url(r'^marathi/codepoint$', views.marathi_codepoint, name='marathi_codepoint'),
    url(r'^marathi/gsub$', views.marathi_gsub, name='marathi_gsub'),
    url(r'^marathi/gpos$', views.marathi_gpos, name='marathi_gpos'),


    url(r'^odia/$', views.odia, name='odia'),
    url(r'^odia/codepoint$', views.odia_codepoint, name='odia_codepoint'),
    url(r'^odia/gsub$', views.odia_gsub, name='odia_gsub'),
    url(r'^odia/gpos$', views.odia_gpos, name='odia_gpos'),


    url(r'^punjabi/$', views.punjabi, name='punjabi'),
    url(r'^punjabi/codepoint$', views.punjabi_codepoint, name='punjabi_codepoint'),
    url(r'^punjabi/gsub$', views.punjabi_gsub, name='punjabi_gsub'),
    url(r'^punjabi/gpos$', views.punjabi_gpos, name='punjabi_gpos'),


    url(r'^tamil/$', views.tamil, name='tamil'),
    url(r'^tamil/codepoint$', views.tamil_codepoint, name='tamil_codepoint'),
    url(r'^tamil/gsub$', views.tamil_gsub, name='tamil_gsub'),
    url(r'^tamil/gpos$', views.tamil_gpos, name='tamil_gpos'),


    url(r'^telugu/$', views.telugu, name='telugu'),
    url(r'^telugu/codepoint$', views.telugu_codepoint, name='telugu_codepoint'),
    url(r'^telugu/gsub$', views.telugu_gsub, name='telugu_gsub'),
    url(r'^telugu/gpos$', views.telugu_gpos, name='telugu_gpos'),
]