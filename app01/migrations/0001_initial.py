# Generated by Django 2.2.9 on 2020-02-01 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='班级名称')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='学生姓名')),
                ('age', models.IntegerField(default=16, verbose_name='学生年龄')),
                ('score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='成绩')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('introduce', models.TextField(verbose_name='学生自我介绍')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('cls', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='stu_cls', to='app01.Class')),
            ],
            options={
                'verbose_name': '学生表',
                'verbose_name_plural': '学生表',
            },
        ),
    ]
