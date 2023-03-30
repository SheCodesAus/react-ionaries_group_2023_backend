from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CustomUserList.as_view()),
    path('<int:pk>/', views.CustomerUserDetail.as_view()),
    path('admin-user/', views.AdminUserView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)