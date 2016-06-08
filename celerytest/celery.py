from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

try:
    aws_access_key = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
except:
    print 'No envs configured'
    raise

broker = 'sqs://{}:{}@'.format(aws_access_key, aws_secret_key)
app = Celery('celerytest', broker=broker)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
