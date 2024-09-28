from django.urls import path
from .views import post_list_view


urlpatterns = [
    path('posts/', post_list_view, name='posts_list')
]