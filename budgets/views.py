from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

class BudgetListView(ListView):
    template_name = 'budget/budget_list.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return

class BudgetDetailView(ListView):
    template_name = 'budget/budget_detail.html'
