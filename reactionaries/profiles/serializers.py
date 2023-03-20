from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    display_name = serializers.CharField(max_length=200)
    bio = serializers.CharField(max_length=None)
    previous_role = serializers.CharField(max_length=200)
    current_role = serializers.CharField(max_length=200)
    profile_image = serializers.URLField()
    birthdate = serializers.DateField()
    pronouns = serializers.CharField(max_length=200)
    gender = serializers.CharField(max_length=200)
    ethnicity = serializers.CharField(max_length=200)
    linkedin_url = serializers.URLField()
    github_url = serializers.URLField()
    is_visible = serializers.BooleanField()
    is_public = serializers.BooleanField()
    allow_contact = serializers.BooleanField()
    challenge = serializers.CharField(max_length=None)
    # user_id = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)



