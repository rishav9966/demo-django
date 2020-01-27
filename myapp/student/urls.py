from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', views.student_show, name='student_show'),
    path('index/', index),
]