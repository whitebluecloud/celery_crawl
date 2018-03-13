BROKER_URL = "amqp://username:password@10.149.169.184:5673//"
CELERY_IMPORTS = ('test_celery.tasks',)
#CELERY_RESULT_BACKEND = 'file:///workspace/celery-test/result'
CELERY_ANNOTATIONS = {'*': {'rate_limit': '10/s'}}
