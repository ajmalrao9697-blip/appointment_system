# bookings/views.py
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Appointment


class CalendarView(LoginRequiredMixin, TemplateView):
    """Displays the calendar page."""
    template_name = 'calendar.html'


class AppointmentListView(LoginRequiredMixin, ListView):
    """Lists all appointments for the logged-in user."""
    model = Appointment
    template_name = 'appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        # Show only appointments for the logged-in user
        return Appointment.objects.filter(client=self.request.user)


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    """Form to create a new appointment."""
    model = Appointment
    fields = ['provider', 'start_time', 'end_time']
    template_name = 'appointment_form.html'

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    """Displays appointment details."""
    model = Appointment
    template_name = 'appointment_detail.html'
    context_object_name = 'appointment'
