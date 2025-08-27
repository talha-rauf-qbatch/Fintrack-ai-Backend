from django.db import models
from django.contrib.auth.models import User

class Logout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    refresh_token = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self) :
        return f'{self.user.username} @ {self.timestamp}'
