from django.urls import path
from .views import BudgetDetailView, BudgetListView

urlpatterns = [
    path('', BudgetListView.as_view(), name='budget_view'),
    path('<int:id>', BudgetDetailView.as_view(), name='transaction_detail'),
]
