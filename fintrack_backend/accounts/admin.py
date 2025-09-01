from django.contrib import admin
from .models import Logout

@admin.register(Logout)
class LogoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'ip_address')  
    readonly_fields = ('timestamp',)    
