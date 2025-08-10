# bookings/admin.py
from django.contrib import admin
from .models import Appointment, ServiceProvider

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'provider', 'start_time', 'status')
    list_filter = ('status', 'provider')
    search_fields = ('client__username', 'provider__user__username')

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('user', 'services')