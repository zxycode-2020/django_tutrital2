from django.urls import path, include
from app01.views import index, article, test_url, student, \
    students, args, reg, xuanran, orm_test, post_cls, get_cls

urlpatterns = [
    path('index/', index),
    path('article/<str:aid>/', article),
    path('test_url/', test_url),
    path('students/', students),             # 学生列表
    path('student/<str:stu_id>/', student),  # 学生单个
    path('args/', args),
    path('reg/', reg),
    path('xuanran/', xuanran),
    path('orm_test/', orm_test),
    path('post_cls/', post_cls),
    path('get_cls/', get_cls),
]
