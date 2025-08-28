from django.contrib import admin
from .models import Income

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "category", "ai_suggested_category", "description", "date", "created_at", "updated_at")
    list_filter = ("category", "date")
    search_fields = ("description", "user__username", "user__email")
    readonly_fields = ("created_at", "updated_at")
