from django.contrib.auth.models import User
from django.db import models

class Budget(models.Model):
    """Class representing Budget objects."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=1024)
    total_budget = models.FloatField()
    remaining_budget = models.FloatField()


class Transaction(models.Model):
    """Class representing Transaction objects"""
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transactions')
    TRANS_TYPES = [('withdrawal', 'Withdrawal'),
                   ('deposit', 'Deposit')]
    type = models.CharField(max_length=1024, choices=TRANS_TYPES)
    amount = models.FloatField()
    description = models.CharField(max_length=1024)
