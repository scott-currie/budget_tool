from django.urls import path
from .views import (
    UserApiView,
    RegisterApiView,
    BudgetListApiView,
    BudgetDetailApiView,
    TransactionListApiView,
    TransactionDetailApiView)
from rest_framework.authtoken import views


urlpatterns = [
    path(
        'user/<int:pk>',
        UserApiView.as_view(),
        name='user_detail'),
    path(
        'register',
        RegisterApiView.as_view(),
        name='register'),
    path(
        'login',
        views.obtain_auth_token),
    path(
        'budget',
        BudgetListApiView.as_view(),
        name='budget_api_list'),
    path(
        'budget/<int:pk>',
        BudgetDetailApiView.as_view(),
        name='budget_api_detail'),
    path(
        'transaction',
        TransactionListApiView.as_view(),
        name='transaction_api_list'),
    path(
        'transaction/<int:pk>',
        TransactionDetailApiView.as_view(),
        name='transaction_api_detail')]
