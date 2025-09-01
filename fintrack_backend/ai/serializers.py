from rest_framework import serializers

class ChatbotQuerySerializer(serializers.Serializer):
    query = serializers.CharField();
