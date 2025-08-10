
# bookings/apps.py
from django.apps import AppConfig

class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'
    
    def ready(self):
        from .tasks import send_reminder_email
        from django_celery_beat.models import PeriodicTask, IntervalSchedule
        import json
        
        # Create schedule if it doesn't exist
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=24,
            period=IntervalSchedule.HOURS,
        )
        
        # Create task if it doesn't exist
        task, created = PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Send daily appointment reminders',
            task='bookings.tasks.send_reminder_email',
            defaults={
                'args': json.dumps([]),
                'kwargs': json.dumps({}),
            }
        )