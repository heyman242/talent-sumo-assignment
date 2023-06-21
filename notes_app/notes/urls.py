from django.urls import path
from .views import UserRegistrationView, LoginView, NotesCreateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('id/<int:user_id>/create/', NotesCreateView.as_view(), name='notescreate'),


]
