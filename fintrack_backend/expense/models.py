from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("Food", "Food"),
        ("Travel", "Travel"),
        ("Bills", "Bills"),
        ("Shopping", "Shopping"),
        ("Health", "Health"),
        ("Entertainment", "Entertainment"),
        ("Education", "Education"),
        ("Rent", "Rent"),
        ("Utilities", "Utilities"),
        ("Transportation", "Transportation"),
        ("Taxes", "Taxes"),
        ("Insurance", "Insurance"),
        ("Debt Repayment", "Debt Repayment"),
        ("Childcare", "Childcare"),
        ("Maintenance", "Maintenance"),
        ("Legal", "Legal"),
        ("Gifts & Donations","Gifts & Donations"),
        ("Pets", "Pets"),
        ("Miscellaneous", "Miscellaneous"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expense")
    description = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "created_at"]

    def __str__(self):
        return f"{self.user.username}: {self.description[:30]} - {self.amount}"
