from django.shortcuts import render
from .models import ElinkStellarAccount

# Create your views here.

def user_for_account(request, account_id):
    return ElinkStellarAccount.objects.get(account=account_id) or ElinkStellarAccount.objects.get(memo=account_id)

def create_user(request):
    pass