from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Logout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "date_joined",
            "last_login",
        ]
        read_only_fields = ["id", "date_joined", "last_login"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]

    def validate_email(self, value):
        if value and User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already in use.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logout
        fields = "__all__"
        read_only_fields = ["user", "timestamp"]
