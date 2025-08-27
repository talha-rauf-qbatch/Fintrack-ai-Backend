# from typing import Any
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# from django.utils import timezone

# class MyTokenObtainSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         self.user.last_login = timezone.now()
#         self.user.save(update_fields=["last_login"])
#         return data 
    
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainSerializer


from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils import timezone
from rest_framework import serializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        identifier = attrs.get("username")  # yahan username/email dono aa sakta hai
        password = attrs.get("password")

        # check if identifier is email
        try:
            if "@" in identifier:
                user = User.objects.get(email__iexact=identifier)
                attrs["username"] = user.username  # JWT ko username chahiye hota hai
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "No user with this email."})

        # call parent validate
        data = super().validate(attrs)

        # update last_login manually
        self.user.last_login = timezone.now()
        self.user.save(update_fields=["last_login"])

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
