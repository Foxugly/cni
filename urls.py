"""cni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from users.views import dashboard

admin.autodiscover()

def custom_404(request):
    return render(request, "404.tpl")

def custom_505(request):
    return render(request, "500.tpl")

urlpatterns = [
    url(r'^$', login_required(dashboard), name='home'),
    url(r'^user/', include('users.urls'), name='users'),
    url(r'^admin/', include(admin.site.urls)),
] + patterns('', (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), )\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'urls.custom_404'
handler500 = 'urls.custom_500'
