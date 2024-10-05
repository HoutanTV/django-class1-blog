from django.urls import path
from .views import post_list_view, PostCreateView, PostListView, login_required


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('create-post/', login_required(PostCreateView.as_view()), name='create_post'),
]