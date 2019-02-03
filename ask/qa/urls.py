from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.not_found, name='index'),
    url(r'^login/$', views.not_found, name='login'),
    url(r'^signup/$', views.not_found, name='signup'),
    url(r'^question/(?P<pk>\d+)/$', views.test, name='question'),
    url(r'^ask/$', views.not_found, name='ask'),
    url(r'^popular/$', views.not_found, name='popular'),
    url(r'^new$', views.not_found, name='new'),
]