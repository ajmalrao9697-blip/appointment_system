# bookings/utils.py
from datetime import datetime, timedelta
from .models import Appointment

def get_available_slots(provider, date):
    # Get existing appointments
    appointments = Appointment.objects.filter(
        provider=provider,
        start_time__date=date,
        status='confirmed'
    ).values_list('start_time', 'end_time')
    
    # Generate available slots
    working_hours = provider.working_hours[date.strftime('%A').lower()]
    start, end = working_hours.split('-')
    start = datetime.combine(date, datetime.strptime(start, '%H:%M').time())
    end = datetime.combine(date, datetime.strptime(end, '%H:%M').time())
    
    slots = []
    current = start
    while current + timedelta(minutes=30) <= end:
        slot_end = current + timedelta(minutes=30)
        if not any(appt[0] <= current < appt[1] for appt in appointments):
            slots.append((current.time(), slot_end.time()))
        current = slot_end
    return slots