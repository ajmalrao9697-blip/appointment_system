# bookings/tables.py
import django_tables2 as tables
from .models import Appointment

class AppointmentTable(tables.Table):
    client = tables.Column(accessor='client.get_full_name')
    service = tables.Column(accessor='service.name')
    duration = tables.Column(accessor='service.duration')
    price = tables.Column(accessor='service.price')
    
    class Meta:
        model = Appointment
        template_name = "django_tables2/bootstrap5.html"
        fields = ('start_time', 'client', 'service', 'duration', 'price', 'status')