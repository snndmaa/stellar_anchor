from decimal import Decimal
from django import forms
from django.http import HttpResponse
from rest_framework.request import Request
from polaris.models import Transaction
from polaris.templates import Template
from polaris.integrations import (
    DepositIntegration,
    WithdrawalIntegration,
    TransactionForm
)


def zzz(request):
    print(dir(Transaction))
    return HttpResponse('<h1>zzz</h1>')