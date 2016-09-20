from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^history/$', views.history, name='history'),
    url(r'^roadmap/$', views.roadmap, name='roadmap'),
    url(r'^hindi/$', views.hindi, name='hindi'),
]