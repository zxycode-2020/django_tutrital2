from django.contrib import admin

# Register your models here.
from app01.models import Student, Class

# 将模型注册到admin
admin.site.register([Student, Class])