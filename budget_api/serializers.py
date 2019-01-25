from django.contrib.auth.models import User
from rest_framework import serializers
from budgets.models import Budget, Transaction


class UserSerializer(serializers.ModelSerializer):
    """Create serialized User objects."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email']
        })
        user.set_password(validated_data['password'])
        user.save()
        return user


class BudgetSerializer(serializers.ModelSerializer):
    """Create serialized Budget objects though the API."""

    class Meta:
        model = Budget
        fields = ('id', 'name', 'total_budget', 'remaining_budget')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    """Create serialized Transaction objects through the API."""
    # return transaction
    budget = serializers.HyperlinkedRelatedField(
        view_name='budget_api_detail', read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'budget', 'type', 'amount', 'description')
