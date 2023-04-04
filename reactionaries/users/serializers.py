from rest_framework import serializers
from django.utils import timezone
from .models import CustomUser
from profiles.serializers import ProfileSerializer
from profiles.models import Profile


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    is_approved = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=True)
    date_joined = serializers.DateTimeField(default=timezone.now)
    is_staff = serializers.BooleanField(default=False)
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
    
class UserNestedSerializer(CustomUserSerializer):
    user_profile = ProfileSerializer (many=True, read_only=True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class CustomUserDetailSerializer(serializers.ModelSerializer):
    """ a detail serializer for our user class """
    profile = UserProfileSerializer()
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'profile',
            'last_login',
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'is_approved',
            'is_staff',
        ]
