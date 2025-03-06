from django.urls import path
from .views import getReceiptPoints, processReceipt

urlpatterns = [
    path('<uuid:receiptId>/points/', getReceiptPoints, name = 'getReceiptPoints'),
    path('process/', processReceipt, name = 'processReceipt')
]