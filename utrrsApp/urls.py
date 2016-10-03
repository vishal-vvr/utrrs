from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),


    url(r'^about/$', views.about, name='about'),


    url(r'^history/$', views.history, name='history'),


    url(r'^roadmap/$', views.roadmap, name='roadmap'),


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


    url(r'^maithili/$', views.maithili, name='maithili'),


    url(r'^malayalam/$', views.malayalam, name='malayalam'),


    url(r'^marathi/$', views.marathi, name='marathi'),


    url(r'^odia/$', views.odia, name='odia'),


    url(r'^punjabi/$', views.punjabi, name='punjabi'),


    url(r'^tamil/$', views.tamil, name='tamil'),


    url(r'^telugu/$', views.telugu, name='telugu'),
]