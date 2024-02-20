from django.urls import path, include 
from django.contrib import admin

urlpatterns = [
    path('admin', admin.sites.urls),
    
    # Main app
    path('', include('photoapp.urls')),
]