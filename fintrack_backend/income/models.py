from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    CATEGORY_CHOICES = [
        ("Salary", "Salary"),
        ("Business", "Business"),
        ("Investment", "Investment"),
        ("Freelancing", "Freelancing"),
        ("Rental Income", "Rental Income"),
        ("Dividends", "Dividends"),
        ("Interest", "Interest"),
        ("Capital Gains", "Capital Gains"),
        ("Pension", "Pension"),
        ("Annuity", "Annuity"),
        ("Social Security", "Social Security"),
        ("Royalties", "Royalties"),
        ("Gambling Winnings", "Gambling Winnings"),
        ("Alimony", "Alimony"),
        ("Child Support", "Child Support"),
        ("Grants", "Grants"),
        ("Scholarship", "Scholarship"),
        ("Tax Refund", "Tax Refund"),
        ("Sale of Assets", "Sale of Assets"),
        ("Gift", "Gift"),
        ("Inheritance", "Inheritance"),
        ("Other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="income")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date","-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.amount} ({self.category})"