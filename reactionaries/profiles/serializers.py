from rest_framework import serializers
from .models import Profile, Project


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
    user = serializers.ReadOnlyField(source='user')

   
    def create(self, validated_data):
        return Profile.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    image = serializers.URLField()
    description = serializers.CharField(max_length=None)
    url = serializers.URLField()
    profile_id = serializers.IntegerField()
    

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProfileDetailSerializer(ProfileSerializer):
    project = ProjectSerializer(many=True, read_only=True)


    def update(self, instance, validated_data):
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.previous_role = validated_data.get('previous_role', instance.previous_role)
        instance.current_role = validated_data.get('current_role', instance.current_role)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.pronouns = validated_data.get('pronouns', instance.pronouns)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.ethnicity = validated_data.get('ethnicity', instance.ethnicity)
        instance.linkedin_url = validated_data.get('linkedin_url', instance.linkedin_url)
        instance.github_url = validated_data.get('github_url', instance.github_url)
        instance.is_visible = validated_data.get('is_visible', instance.is_visible)
        instance.is_public  = validated_data.get('date_created', instance.is_public )
        instance.allow_contact = validated_data.get('allow_contact', instance.allow_contact)
        instance.challenge = validated_data.get('challenge', instance.challenge)
        instance.save()
        return instance


class ProjectDetailSerializer(ProjectSerializer):
    

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image ', instance.image )
        instance.url = validated_data.get('url', instance.url)
        instance.profile = validated_data.get('profile', instance.profile) 
        instance.save()
        return instance

  


