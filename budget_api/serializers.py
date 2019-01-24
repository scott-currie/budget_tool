from django.contrib.auth.models import User
from rest_framework import serializers
from budgets.models import Budget, Transaction


class UserSerializer(serializers.ModelSerializer):
    """Create serialized User objects."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

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
        fields = ('name', 'total_budget', 'remaining_budget')

    # def create(selfself, validated_data):
    #
    #
    #     return budget


class TransactionSerializer(serializers.ModelSerializer):
    """Create serialized Transaction objects through the API."""
    # return transaction
    class Meta:
        model = Transaction
        fields = ('type', 'amount', 'description')
