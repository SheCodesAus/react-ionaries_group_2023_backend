from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer, ProfileDetailSerializer
from django.http import Http404
from rest_framework import status, generics



class ProfileList(APIView):

    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProfileDetail(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileDetailSerializer(profile)
        return Response(serializer.data)

    def put(self,request,pk):
        profile = self.get_object(pk)
        data = request.data
        serializer = ProfileDetailSerializer(
            instance=profile,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request,id=None):
        profile = self.get_object(id=id)
        profile.delete()
        return Response(status.HTTP_204_NO_CONTENT)




class ProjectList(APIView):

    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )




