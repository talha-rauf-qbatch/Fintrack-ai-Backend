from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import ChatbotQuerySerializer
from .services import financial_chatbot

class FinancialChatbotView(APIView):
    
    def post(self, request):
        serializer = ChatbotQuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data["query"]
            advice = financial_chatbot(query)
            return Response({"advice": advice}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            