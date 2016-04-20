from django.conf.urls import url
from . import views

urlpatterns = [
   #url(r'^$', views.profile_project),
   url(r'^$', views.project_page),
   url(r'^profile/$', views.profile_page),
   url(r'^global/$', views.global_page)
]
