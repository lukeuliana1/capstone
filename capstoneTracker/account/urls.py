from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = patterns('',
   url(r'^$', RedirectView.as_view(url='profile', permanent=False), name='index'),			
   url(r'^login/$', views.login),
   url(r'^logout/$', views.logout),
   url(r'^register/$', views.register_employee),
   url(r'^confirm/$', views.confirm_email),
   url(r'^profile/$', views.profile),
   url(r'^profile/.*$', views.profile)
   )
