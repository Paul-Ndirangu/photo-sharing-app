# photoapp/urls.py
from django.urls import path

from .views import (
    PhotoListView,
    PhotoTagListView,
    PhotoDeleteView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDetailView    
)

# Empty patterns
urlpatterns = [
    path("", PhotoListView.as_view(), name="list"),
    path('tag/<slug:tag>/', PhotoTagListView.as_view(), name="tag"),
    path('photo/<int:pk>/', PhotoTagListView.as_view(), name="detail"),
    path('photo/create/', PhotoCreateView.as_view(), name="create"),
    path('photo/<int:pk>/', PhotoUpdateView.as_view(), name="update"),
    path('photo/<int:pk>/', PhotoDeleteView.as_view(), name="delete"),
]