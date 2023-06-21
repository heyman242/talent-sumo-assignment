from django.urls import path
from .views import UserRegistrationView, LoginView, NotesCreateView,NotesListView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('id/<int:user_id>/create/', NotesCreateView.as_view(), name='notescreate'),
    path('id/<int:user_id>/list/', NotesListView.as_view(), name='noteslist'),


]
