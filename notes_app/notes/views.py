from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note, RegisteredUser
from .serializers import NoteSerializer, RegisteredUserSerializer, LoginSerializer


# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = RegisteredUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            return Response({"message": "Login successful", "user_id": user_id})
        else:
            return Response(serializer.errors, status=400)


class NotesCreateView(APIView):
    def post(self, request, user_id):
        user = RegisteredUser.objects.get(pk=user_id)
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotesListView(APIView):
    def get(self, request, user_id):
        user = RegisteredUser.objects.get(pk=user_id)
        notes = Note.objects.filter(user=user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)


class NotesUpdateView(APIView):

    def put(self, request, user_id, note_id):
        note = Note.objects.get(id=note_id, user_id=user_id)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

