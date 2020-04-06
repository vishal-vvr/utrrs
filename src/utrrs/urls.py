from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('utrrs/', include('utrrsApp.urls')),
    path('', views.index, name="index_page"),
    path('about', views.about, name="about_page"),
    path('checkfont', views.checkfont, name="checkfont_page"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
