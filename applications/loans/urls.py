from django.urls import path
from . import views

urlpatterns = [
    path('loans/list/', views.LoanListAPIView.as_view(), name='loans_list'),
]