from django.urls import path

from . import views

# URL Reverse에서 namespace 역할
# app_name = 'blog1'

urlpatterns = [
    path('', views.post_list, name='post_list'),
]