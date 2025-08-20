from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.description} - {self.amount} ({self.transaction_type})"
    
    @property
    def is_profit(self):
        return self.transaction_type == 'income'
    
    @property
    def is_loss(self):
        return self.transaction_type == 'expense'
    
    class Meta:
        ordering = ['-date']
