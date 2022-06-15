from django.shortcuts import render
from django.views.generic.list import ListView
from receipts.models import Receipt
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"
    context_object_name = "receiptlist"
    fields = ["vendor", "total", "tax", "date", "category", "account"]

    def get_queryset(self):
        return Receipt.objects.filter(user=self.request.user)
