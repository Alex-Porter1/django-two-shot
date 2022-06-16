from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from receipts.models import Account, ExpenseCategory, Receipt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"
    context_object_name = "receiptlist"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    template_name = "receipts/create.html"
    fields = ["vendor", "total", "tax", "date", "category", "account"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.purchaser = self.request.user
        item.save()
        return redirect("home")


class ExpenseCategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = "expense_categories/list.html"
    context_object_name = "expensecategory"

    def get_queryset(self):
        return ExpenseCategory.objects.filter(owner=self.request.user)


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "accounts/list.html"
    context_object_name = "accounts"

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    template_name = "expense_categories/create.html"
    fields = ["name"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("list_categories")
