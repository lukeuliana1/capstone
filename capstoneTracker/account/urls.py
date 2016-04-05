from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
   url(r'^$', RedirectView.as_view(url='profile', permanent=False), name='index'),			
   url(r'^login/$', views.login),
   url(r'^logout/$', views.logout),
   url(r'^register/$', views.register_employee),
   url(r'^confirm/$', views.confirm_email),
   url(r'^password-change/$', views.password_change),
   url(r'^forgot-password/$', views.forgot_password),
   url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
      views.password_reset_confirm, name='password_reset_confirm'),
   url(r'^profile/$', views.profile, name='profile'),
   url(r'^profile/.*$', views.profile) #Not implemented yet (see other profiles)
   ]
