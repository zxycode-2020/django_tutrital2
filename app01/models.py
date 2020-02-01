from django.db import models
from datetime import datetime


class Student(models.Model):  # 一定要继承
    # CharField为字符串类型，必须有max_length设置最大长度,verbose_name在django后台显示该英文字段的中文意思
    name = models.CharField(max_length=30, verbose_name="学生姓名")
    # IntegerField整型
    age = models.IntegerField(default=16, verbose_name="学生年龄")
    # DecimalField浮点型，max_digits=5表示整数部分和小数位数之和不大于5，decimal_places表示小数的最大位数，
    # null=True表示字段可以为空，blank=True表示在admin后台中该数据栏可以为空
    score = models.DecimalField(verbose_name='成绩', max_digits=5, decimal_places=2, null=True, blank=True)  #
    # EmailField该字段必须符合邮箱格式
    email = models.EmailField(verbose_name='邮箱', null=True, blank=True)
    # TextField 字段位文本类型，长度没有限制
    introduce = models.TextField(verbose_name="学生自我介绍")
    # DateTimeField为日期类型，auto_now_add=True该条数据创建的时间，数据更新时，时间数值不变
    # auto_now=True该条数据创建的时间，数据更新时，时间数值也会改变
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    # ForeignKey一对多外键，比如一个班级有多个学生，就属于一对多，外键要放到"多"的那张表,
    # related_name是对外键取别名，常用在django的orm反向查询中
    cls = models.ForeignKey('Class', related_name="stu_cls", null=True, on_delete=models.PROTECT)

    # 下面是django后台字段显示控制
    class Meta:
        verbose_name_plural = verbose_name = "学生表"

    def __str__(self):
        return self.name


class Class(models.Model):  # 班级表
    name = models.CharField(verbose_name='班级名称', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '班级'
