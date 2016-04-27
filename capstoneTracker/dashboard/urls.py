from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^profile/$', views.profile_page),
   url(r'^global/$', views.global_page),
   url(r'^$', views.project_page_user),
   url(r'^project/.+$', views.project_page_request),
   #url(r'^.+$', views.project_page_request)
]
