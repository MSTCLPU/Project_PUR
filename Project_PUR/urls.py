"""Project_PUR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#Main Project Url

from django.conf.urls import url
from django.contrib import admin
from account import views as accountview


urlpatterns = [
	url(r'^$',accountview.false),
	url(r'^login/$',accountview.loginit,name='login'),
	url(r'^logout/$',accountview.logoutit,name='logout'),
	url(r'^purchecker/$',accountview.checkpur,name='checkpur'),
	url(r'^purgen/$',accountview.UploadPURForm,name='uploadpur'),
	url(r'^test/$',accountview.test,name='test'),
	url(r'^generate_cert/(?P<pur>[0-9A-Za-z]+)/(?P<name>[0-9A-Za-z ]+)$',accountview.cert,name='printcert'),
	url(r'^android/(?P<pur_id>[0-9A-Za-z]+)/(?P<name>[0-9A-Za-z]+)$',accountview.androidapi),
	url(r'^signup/$',accountview.createaccount,name='createaccount'),
	url(r'^profile/$',accountview.dashboard,name='profile'),
]
