from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^history/$', views.history, name='history'),
    url(r'^roadmap/$', views.roadmap, name='roadmap'),
    url(r'^assamese/$', views.assamese, name='assamese'),
    url(r'^bengali/$', views.bengali, name='bengali'),
    url(r'^german/$', views.german, name='german'),
    url(r'^gujarati/$', views.gujarati, name='gujarati'),
    url(r'^hindi/$', views.hindi, name='hindi'),
]