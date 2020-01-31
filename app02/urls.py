from django.urls import path, include
from app02.views import index, article, test_url, caijing, yule

urlpatterns = [
    path('index/', index),
    path('article/<str:aid>/', article),
    path('test_url/', test_url),
    path('caijing/', caijing),
    path('yule/', yule),

]