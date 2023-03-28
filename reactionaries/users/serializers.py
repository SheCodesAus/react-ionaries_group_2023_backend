from rest_framework import serializers
from django.utils import timezone
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    is_approved = serializers.BooleanField()
    is_active = serializers.BooleanField()
    date_joined = serializers.DateTimeField(default=timezone.now)
    is_admin = serializers.BooleanField()
    password = serializers.CharField(write_only = True)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class UserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance