from ..factories import BudgetFactory, TransactionFactory, UserFactory
from django.test import TestCase


class TestBudgetModel(TestCase):
    def setUp(self):
        self.budget = BudgetFactory(name='Test Budget')

    def test_default_budget_attrs(self):
        self.assertEqual(self.budget.name, 'Test Budget')


class TestTransactionModel(TestCase):
    def setUp(self):
        self.user = UserFactory(username='trans_test_user')
        self.budget = BudgetFactory(user=self.user)
        self.transaction = TransactionFactory(budget=self.budget)

    def test_default_transaction_attrs(self):
        self.assertEqual(self.user.username, 'trans_test_user')
