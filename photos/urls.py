from django.urls import re_path
from . import views 

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'image/', views.one_image, name='image'),
    re_path(r'^search/', views.search, name='search'),
]