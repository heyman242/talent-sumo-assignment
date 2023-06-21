from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note, RegisteredUser
from .serializers import NoteSerializer,RegisteredUserSerializer, LoginSerializer


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