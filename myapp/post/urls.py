from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # Ajax tuorial
    path('', views.index, name='index'),
    path('like/', views.like, name='like'),
]