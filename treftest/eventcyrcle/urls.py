from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import redirect
from .views import EventListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', EventListView.as_view(), name='event-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='event-about'),
    path('testinfopage/', views.testinfopage, name='event-testinfopage'),
]
