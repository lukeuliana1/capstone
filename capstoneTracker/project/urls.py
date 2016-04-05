from django.conf.urls import url
from . import views

urlpatterns = [
   #url(r'^$', views.profile_project),
   url(r'^create-project/$', views.create_project),
   #url(r'^.*$', views.show_project),
   ]
