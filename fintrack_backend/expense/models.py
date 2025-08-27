from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("Food", "Food (Groceries, Dining Out, Snacks, Beverages)"),
        ("Travel", "Travel (Flights, Accommodation, Transport, Activities, Souvenirs)"),
        ("Bills", "Bills (Electricity, Water, Gas, Internet, Phone, Insurance)"),
        ("Shopping", "Shopping (Clothing, Electronics, Home Goods, Beauty Products, Toys)"),
        ("Health", "Health (Doctor Visits, Medications, Therapy, Fitness)"),
        ("Entertainment", "Entertainment (Movies, Concerts, Games, Hobbies, Books)"),
        ("Education", "Education (Tuition, Books, Online Courses, Workshops, Student Loans)"),
        ("Rent", "Rent (Apartment, Mortgage, Roommate Share, Storage, Parking)"),
        ("Utilities", "Utilities (Electricity, Water, Gas, Internet, Trash Services)"),
        ("Transportation", "Transportation (Fuel, Car Maintenance, Public Transport, Taxis)"),
        ("Taxes", "Taxes (Income Tax, Property Tax, Sales Tax, Tax Penalties)"),
        ("Insurance", "Insurance (Health, Life, Auto, Home, Travel)"),
        ("Debt Repayment", "Debt Repayment (Credit Cards, Loans, Mortgages, Personal Loans)"),
        ("Childcare", "Childcare (Daycare, Babysitting, School Fees, Activities)"),
        ("Maintenance", "Maintenance (Home Repairs, Car Repairs, Appliance Replacement)"),
        ("Legal", "Legal (Lawyer Fees, Court Costs, Legal Settlements)"),
        ("Gifts & Donations",
         "Gifts & Donations (Birthday, Christmas, Charitable Donations)"),
        ("Pets", "Pets (Food, Veterinary, Supplies, Boarding)"),
        ("Misc", "Miscellaneous (Gifts, Charity, Pet Care, Unexpected Repairs, Subscriptions)"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expense")
    description = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)
    ai_suggested_category = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "created_at"]

    def __str__(self):
        return f"{self.user.username}: {self.description[:30]} - {self.amount}"
