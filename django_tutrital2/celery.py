from __future__ import absolute_import, unicode_literals

import logging
import os

from celery import Celery
from django.conf import settings


logger = logging.getLogger(__name__)
# 固定设置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutrital2.settings')
# 实例化 celery
app = Celery('django_tutrital2',    # 你这个django项目的名称
             broker=settings.REDIS_URL,  # celery 的broker
             backend=settings.REDIS_URL,  # celery 的backend
             include=["app01.tasks"      # 定时脚本所在目录
                      ]
             )

app.config_from_object('django.conf:settings')   # 固定设置
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)  # 固定设置


#  自定义的定时任务脚本
@app.task()
def test_beat():
    logger.info("bang!")
    print("bang")
    return "bang"



