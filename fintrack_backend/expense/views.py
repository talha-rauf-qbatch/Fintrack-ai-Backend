from rest_framework import generics, permissions
from .models import Expense
from .serializers import ExpenseSerializer
from ai.services import suggest_expense_category


class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        expense = serializer.save(user=self.request.user)

        try:
            suggest_category = suggest_expense_category(expense.description)

            if not expense.category or expense.category == "Misc":
                expense.category = suggest_category
                
            expense.ai_suggested_category = suggest_category
            expense.save(update_fields=["category", "ai_suggested_category"])

        except Exception as err:
            print("LLM Error in Expense:", err)


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
