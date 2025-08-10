# bookings/filters.py
import django_filters
from .models import Appointment
from django.utils import timezone
from datetime import timedelta

class AppointmentFilter(django_filters.FilterSet):
    date_range = django_filters.ChoiceFilter(
        choices=[
            ('today', 'Today'),
            ('week', 'This Week'),
            ('month', 'This Month'),
            ('year', 'This Year'),
        ],
        method='filter_date_range',
        label='Date Range'
    )
    
    status = django_filters.MultipleChoiceFilter(
        choices=Appointment.STATUS_CHOICES
    )
    
    class Meta:
        model = Appointment
        fields = ['status', 'service']
    
    def filter_date_range(self, queryset, name, value):
        now = timezone.now()
        if value == 'today':
            return queryset.filter(start_time__date=now.date())
        elif value == 'week':
            start = now - timedelta(days=now.weekday())
            end = start + timedelta(days=6)
            return queryset.filter(start_time__range=[start, end])
        elif value == 'month':
            return queryset.filter(
                start_time__year=now.year,
                start_time__month=now.month
            )
        elif value == 'year':
            return queryset.filter(start_time__year=now.year)
        return queryset