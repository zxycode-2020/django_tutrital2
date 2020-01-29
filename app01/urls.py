from django.urls import path, include
from app01.views import index, article, test_url

urlpatterns = [
    path('index/', index),
    path('article/<str:aid>/', article),
    path('test_url/', test_url),
]