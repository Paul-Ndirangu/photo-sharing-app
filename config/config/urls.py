
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Main app
    path('', include('photoapp.urls')),
]
