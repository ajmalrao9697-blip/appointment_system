from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appointment_system.settings')
app = Celery('appointment_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()