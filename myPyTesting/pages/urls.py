# pages/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('posts/', views.PostsPageView.as_view(), name='posts'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]