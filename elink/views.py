from django.shortcuts import render
from .models import ElinkStellarAccount, ElinkUser, ElinkUserKYC

# Create your views here.

def user_for_account(account_id):
    stellar_account = ElinkStellarAccount.objects.get(account=account_id)\
    or\
    ElinkStellarAccount.objects.get(memo=account_id)
    
    return ElinkUser.objects.get(id=stellar_account.user.id)

def create_user(info):
    print('Create User => f{info}')

def update_user_kyc(form, user):
    ElinkUserKYC.objects.create(
        user=user,
        address_1=form.cleaned_data['address_1'],
        address_2=form.cleaned_data['address_2'],
        country=form.cleaned_data['country'],
        city=form.cleaned_data['city'],
        state=form.cleaned_data['state'],
        zip_code=form.cleaned_data['zip_code']
    ) 
    

def calculate_fee(transaction):
    print(transaction)