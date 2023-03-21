from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('profile/', views.ProfileList.as_view()),
    path('profile/<int:pk>/', views.ProfileDetail.as_view()),
    path('project/', views.ProjectList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)