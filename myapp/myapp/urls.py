"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', index),
    path('redirect/', my_app),
    # path('django/', RedirectView.as_view(url = ‘https://data-flair.training/blogs/category/django/’)),
    path('django/', RedirectView.as_view(url = "https://facebook.com")),
    path('facebook/', Gothrough.as_view()),
    path('student/', include('student.urls')),

    # for homepage
    path('', include('home.urls')),

        ###############infinite loop through###############
    path('inf1/', inf1),
    path('inf2/', inf2),
        ###############infinite loop through###############

    path('setcookie/', setcookie),
    path('getcookie/', getcookie),
    path('delcookie/', delcookie),

    # path for test cookie for session purpose
    path('testcookie/', cookie_session),
    path('deltestcookie/', cookie_delete),

    # create and access session
    path('create/', create_session),
    path('access/', access_session),
    path('delete/', del_session),

    # Send email through subscribe app
    path('subscribe/', include('subscribe.urls')),
    
    # registration for form validation purpose
    path('registration/', include('registration.urls')),

    # upload file
    path('upload/', include('profile_maker.urls')),

    # Ajax tutorials
    path('ajax/', include('post.urls')),
]
# /home/rishav/Desktop/env/myapp/subscribe/urls.py