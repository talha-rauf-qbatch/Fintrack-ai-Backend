from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("user", "description", "amount", "date", "category", "ai_suggested_category", "created_at")
    list_filter = ("category", "date")
    search_fields = ("description", "user__username", "user__email")
    readonly_fields = ("created_at", "updated_at")
