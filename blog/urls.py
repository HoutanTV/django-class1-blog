from django.urls import path
from .views import post_list_view, PostCreateView, PostListView, login_required, post_view, post_search_view


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('create-post/', login_required(PostCreateView.as_view()), name='create_post'),
    path('post/<int:id>/', post_view, name='post_page'),
    path('post/search/', post_search_view, name='post_search')
]
