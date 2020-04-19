from django.urls import path

from .views import post_list,post_details

app_name = 'blog_app'
urlpatterns = [
    path('',post_list, name='post_list'),
    path('details/<int:pk>/',post_details, name='post_details'),
]
