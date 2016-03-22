from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
   #url(r'^$', views.profile_project),
   url(r'^create-project/$', views.create_project),
   #url(r'^.*$', views.show_project),
   )
