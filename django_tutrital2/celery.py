from __future__ import absolute_import, unicode_literals

import datetime
import logging
import os

from celery import Celery, shared_task
from django.conf import settings

# from django_tutrital2.settings import BACKUP_PATH
# from libs.datetimes import date_to_str
# from libs.environment import ENV

logger = logging.getLogger(__name__)
# current_env = ENV()
#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutrital2.settings')

app = Celery('django_tutrital2',
             broker=settings.REDIS_URL,
             backend=settings.REDIS_URL,
             include=["app01.tasks"
                      ]
             )

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task()
def test_beat():
    logger.info("bang!")
    print("bang")
    return "bang"



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


