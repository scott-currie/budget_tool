import factory
from django.contrib.auth.models import User
import random
from budgets.models import Budget, Transaction


class UserFactory(factory.django.DjangoModelFactory):
    """Create test User objects."""

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BudgetFactory(factory.django.DjangoModelFactory):
    """Create test Budget objects."""

    class Meta:
        model = Budget

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('word')
    total_budget = random.random() * 5000
    remaining_budget = total_budget - random.random() * total_budget


class TransactionFactory(factory.django.DjangoModelFactory):
    """Create test Transaction objects."""

    class Meta:
        model = Transaction
    budget = factory.SubFactory(BudgetFactory)
    type = random.choice(Transaction.TRANS_TYPES)[0]
    amount = random.random() * 20
    description = factory.Faker('paragraph')
