from django.urls import path
from .views import test_view, register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('test/', test_view, name='test')
]