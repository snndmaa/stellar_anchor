import decimal
from django.shortcuts import render
from .models import ElinkStellarAccount, ElinkUser, ElinkUserKYC, ElinkPayment

# Create your views here.

def user_for_account(account_id):
    #to get the user account linked to a stellar public key

    stellar_account = ElinkStellarAccount.objects.get(account=account_id)\
    or\
    ElinkStellarAccount.objects.get(memo=account_id)
    
    return ElinkUser.objects.get(id=stellar_account.user.id)

def create_user(info):
    #not in use presently

    print('Create User => f{info}')

def update_user_kyc(form, user):
    #attach more info to a specific user account

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
    # not in use presently
    
    fee = (transaction.amount_in) * decimal.Decimal(10/100)

    return fee

def is_valid_payment_amount(amount_in):
    #for test just check if amount_in is at least $50

    if amount_in > 50:
        return True
    else:
        False

def initiate_refund(transaction):
    #Send User back his money using transaction model

    print('INITIATE REFUND')

def submit_payment(transaction):
    #use transaction to create and update a payment model

    try:
        payment = ElinkPayment.objects.get(transaction=transaction)
        payment.status = 'DELIVERED'
        payment.save()
        return payment

    except ElinkPayment.DoesNotExist:
        payment = ElinkPayment.objects.create(
            transaction=transaction,
        )
        return payment


def get_payment(transaction):
    #return payment instance to poll_outgoing_transactions

    return ElinkPayment.objects.get(transaction=transaction)
