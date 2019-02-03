from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.not_found, name='index'),
    path(r'^login/$', views.not_found, name='login'),
    path(r'^signup/$', views.not_found, name='signup'),
    path(r'^question/(?P<pk>\d+)/$', views.test, name='question'),
    path(r'^ask/$', views.not_found, name='ask'),
    path(r'^popular/$', views.not_found, name='popular'),
    path(r'^new$', views.not_found, name='new'),
]