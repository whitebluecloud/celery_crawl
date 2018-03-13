from __future__ import absolute_import
from celery import Celery
app = Celery('test_celery',backend='rpc://', broker='amqp://username:password@10.149.169.184:5673',include=['test_celery.tasks'])
#app = Celery('test_celery')
