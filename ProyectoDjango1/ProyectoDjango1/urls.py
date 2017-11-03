from django.conf.urls import include
from django.contrib import admin

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views


from django.contrib.auth.views import login, logout_then_login

#configuracion de media
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
##################3


urlpatterns = [
    # Examples:
	url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
	
	url(r'^$', login, {'template_name': 'app/login.html'},name='login'),
   	url(r'^logout/$',logout_then_login, name = 'logout'),
	url(r'^signup/$',app.views.Signup.as_view(),name="Signup_view"),
	url(r'^wsdenuncia/$',app.views.wsDenuncia, name='wsDenucia_view'),
	url(r'^denuncia/$', app.views.Denuncia, name='denuncia_view'),
	url(r'^accounts/', include('allauth.urls')),
	#url(r'^facebook/$',app.views.Facebook_view.as_view(),name='facebook_view'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)