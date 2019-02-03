from django.urls import path
from . import views

urlpatterns = [
    path('', views.not_found, name='index'),
    path('login/', views.not_found, name='login'),
    path('signup/', views.not_found, name='signup'),
    path('question/(?P<pk>\d+)/', views.test, name='question'),
    path('ask/', views.not_found, name='ask'),
    path('popular/', views.not_found, name='popular'),
    path('new', views.not_found, name='new'),
]