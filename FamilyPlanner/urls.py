"""FamilyPlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from accounts import views as accounts_views
# from calendar import views as calender_views
from familycalender import views as familycalender_views
from todolist import views as todolist_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/', accounts_views.login),
    url(r'register/', accounts_views.register),
    url(r'user/',accounts_views.index),
    url(r'^calender/',familycalender_views.familycalender_index),
    url(r'addmember/',accounts_views.add_memnbers),
    url(r'family-calender/',todolist_views.family_calender),
    url(r'my-calender/',todolist_views.my_todo),
    url(r'add-task/',todolist_views.create_new_todo)
]
