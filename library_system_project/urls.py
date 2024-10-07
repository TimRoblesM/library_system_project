from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('applications.books.urls')),
    path('loans/', include('applications.loans.urls')),
    path('users/', include('applications.users.urls')),
]
