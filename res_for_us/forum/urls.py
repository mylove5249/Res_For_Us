"""res_for_us URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from .views import ForumLV, ForumCreateView, ForumDV, SearchView
from django.views.decorators.csrf import csrf_exempt

app_name='forum'

urlpatterns = [
    path('', ForumLV.as_view(), name='index'),
    # path('list/',View.as_view(), name='forum_list'),
    re_path(r'^forum/(?P<slug>[-\w]+)/$', ForumDV.as_view(), name="forum_detail"),
    path('add/', ForumCreateView.as_view(), name="add",),
    path('search/',csrf_exempt(SearchView.as_view()), name='search_result'),

]