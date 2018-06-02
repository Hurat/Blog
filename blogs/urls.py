"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Page for adding a new post
    path('new_post/', views.new_post, name='new_post'),

    # Page for viewing a single post
    path('post/<int:post_id>/', views.post, name='post'),

    # Page for editing an post
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]