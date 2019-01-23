from django.forms import ModelForm
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    """"Class defining a form for creating Budget objects."""
    class Meta:
        model = Budget
        fields = ['name', 'total_budget']


class TransactionForm(ModelForm):
    """Class defining a form for creating Transaction objects."""
    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'description']

