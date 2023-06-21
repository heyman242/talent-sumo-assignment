from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note, RegisteredUser
from .serializers import NoteSerializer,RegisteredUserSerializer


# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = RegisteredUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)