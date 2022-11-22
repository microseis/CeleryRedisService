import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailer.settings')

app = Celery('mailer')
app.config_from_object('django.conf:settings',
                       namespace='CELERY')
#app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'send-email-every-1-min': {
#         'task': 'main.tasks.send_bulk_email',
#         'schedule': crontab(minute='*/1')
#
#     }
# }
