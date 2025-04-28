from django.db import models
from django.core.validators import MinValueValidator 

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Rent', 'Rent'),
        ('Utilities', 'Utilities'),
        ('Entertainment', 'Entertainment'),
        ('Travel', 'Travel'),
        ('Shopping', 'Shopping'),
        ('Others', 'Others'),
    ]

    title = models.CharField(max_length=200)
    
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)] 
        )
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
   
    notes = models.TextField(blank=True, null=True)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"{self.title} - {self.amount} on {self.date}"

