from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'profile/(?P<user_pk>\d+)/$', views.profile_detail, name='profile_detail'),
    url(r'profile/(?P<profile_pk>\d+)/edit/$', views.profile_edit, name='profile_edit'),
    url(r'profile/(?P<profile_pk>\d+)/change_password/$', views.profile_change_password, name='profile_change_password'),
    url(r'sign_in/$', views.sign_in, name='sign_in'),
    url(r'sign_up/$', views.sign_up, name='sign_up'),
    url(r'sign_out/$', views.sign_out, name='sign_out'),
]