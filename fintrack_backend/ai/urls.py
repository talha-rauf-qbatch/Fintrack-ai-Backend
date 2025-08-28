from django.urls import path
from .views import FinancialChatbotView

urlpatterns = [
    path("chatbot/", FinancialChatbotView.as_view(), name="financial-chatbot"),
]
