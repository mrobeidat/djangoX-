
  
from django.urls import path
from .views import (
                                SnackCreateView,
                                SnackListView,
                                SnackDetailView,
                                SnackDeleteView,
                                SnackUpdateView
)

urlpatterns = [
    path('' ,SnackListView.as_view(), name='snacks'),
    path('<int:pk>/' ,SnackDetailView.as_view(), name='snack-details'),
    path('create/' ,SnackCreateView.as_view(), name='create-snack'),
    path('<int:pk>/update/' ,SnackUpdateView.as_view(), name='update-snack'),
    path('delete/<int:pk>' ,SnackDeleteView.as_view(), name='delete-snack'),
]