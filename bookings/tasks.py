# bookings/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import Appointment

@shared_task
def send_confirmation_email(appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    send_mail(
        'Appointment Confirmation',
        f'Your appointment is confirmed for {appointment.start_time}',
        'noreply@example.com',
        [appointment.client.email],
        fail_silently=False,
    )

@shared_task
def send_reminder_email(appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    send_mail(
        'Appointment Reminder',
        f'Reminder: You have an appointment tomorrow at {appointment.start_time}',
        'noreply@example.com',
        [appointment.client.email],
        fail_silently=False,
    )