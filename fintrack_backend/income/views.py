from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Income
from .serializers import IncomeSerializer
from ai.services import suggest_income_category


class IncomeListCreateView(generics.ListCreateAPIView):
    serializer_class = IncomeSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        income = serializer.save(user=self.request.user)

        try:
            suggest_category = suggest_income_category(income.description)

            if not income.category or income.category == "Other":
                income.category = suggest_category

            income.ai_suggested_category = suggest_category
            income.save(update_fields=["category", "ai_suggested_category"])

        except Exception as err:
            print("LLM Error in Income:", err)


class IncomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)