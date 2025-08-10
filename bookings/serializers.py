from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ServiceProvider, Appointment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class ServiceProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ServiceProvider
        fields = ["id", "user", "services", "working_hours"]


class AppointmentSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    provider = ServiceProviderSerializer(read_only=True)

    provider_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceProvider.objects.all(),
        source="provider",
        write_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "client",
            "provider",
            "provider_id",
            "start_time",
            "end_time",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data["client"] = request.user
        return super().create(validated_data)
