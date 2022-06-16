from django.urls import path
from receipts.views import (
    AccountListView,
    ReceiptCreateView,
    ReceiptListView,
    ExpenseCategoryListView,
)

urlpatterns = [
    path("", ReceiptListView.as_view(), name="home"),
    path("create/", ReceiptCreateView.as_view(), name="create_receipt"),
    path(
        "categories/",
        ExpenseCategoryListView.as_view(),
        name="list_categories"),
    path(
        "accounts/",
        AccountListView.as_view(), name="list_accounts"
    ),
]
