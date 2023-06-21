from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    # path('notes/', NoteListAPIView.as_view(), name='note-list'),
]
