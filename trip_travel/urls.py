"""trip_travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from home_page.urls import *
from home_page.views import *
from registration.views import *
from login.views import *
from comment.views import *
from sampark.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^home_page/',include('home_page.urls',namespace='home_page')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$',register,name='register'),
    url(r'^login/$',user_login,name='user_login'),
    url(r'^logout/$',user_logout,name='logout'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^suggest/$',suggest,name='suggest'),
    url(r'^countries_create/$',CountriesCreateView.as_view(),name='country_create'),
    url(r'^countries_update/(?P<pk>[-\w{}.-]{1,4})$',CountriesUpdateView.as_view(),name='countries_update'),
    url(r'^countries_detail/(?P<pk>[-\w{}.-]{1,4})/$', CountriesDetailView.as_view(), name='detail'),
    url(r'^countries_list/$',CountriesListView.as_view(), name='list'),
    url(r'^countries_delete/(?P<pk>[-\w{}.-]{1,4})$',CountriesDeleteView.as_view(),name='countries_delete'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
