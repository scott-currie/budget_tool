from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, User, TransactionSerializer, BudgetSerializer
from rest_framework.authentication import TokenAuthentication
from budgets.models import Budget, Transaction


class UserApiView(generics.RetrieveAPIView):
    """CBV to handle requests for users on REST API.

    """
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class RegisterApiView(generics.CreateAPIView):
    """CBV to handle registration requests on REST API.

    """
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class BudgetListApiView(generics.ListCreateAPIView):
    """List or create Budget objects in API."""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class BudgetDetailApiView(generics.RetrieveAPIView):
    """View a specific Budget object.

    """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(id=self.kwargs['pk'])


class TransactionListApiView(generics.ListCreateAPIView):
    """List or create Transaction objects filtered by budget.

    """
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(id=self.kwargs['pk'])


class TransactionDetailApiView(generics.RetrieveAPIView):
    """View a specific Transaction object."""
    pass
