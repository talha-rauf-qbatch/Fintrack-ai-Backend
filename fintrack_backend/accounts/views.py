from django.shortcuts import render
from rest_framework import generics, permissions ,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer, UserSerializer
from .models import Logout

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        ser = RegisterSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    
class MeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        ip = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR"))
        ua = request.META.get("HTTP_USER_AGENT", "")
        refresh = request.data.get("refresh")

        Logout.objects.create(
            user = user,
            ip_address = (ip.split(",")[0].strip() if ip else None),
            user_agent = ua,
            refresh_token = refresh
        )
        return Response({"message": "Logout recorded.Clear tokens on client."}, status=status.HTTP_200_OK)