from django.urls import path
from . import views

urlpatterns = [
    path('users/list/', views.UserProfileListAPIView.as_view(), name='users_list'),    
]