from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from receipts.models import Receipt
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
        item.user_property = self.request.user
        item.save()
        return redirect("home")
