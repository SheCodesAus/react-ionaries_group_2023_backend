from rest_framework import serializers
from django.utils import timezone
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    is_approved = serializers.BooleanField()
    is_active = serializers.BooleanField()
    date_joined = serializers.DateTimeField(default=timezone.now)
    password = serializers.CharField(max_length=200)
    # username = serializers.CharField(max_length=200, default=" ")

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
