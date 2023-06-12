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
    # print(f'FEE:{transaction.amount_in}')
    # fee = (transaction.amount_in) * decimal.Decimal(10/100)

    return 3.45

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
        payment.status = 'DELIVERED'
        payment.save()
        return payment


def get_payment(transaction):
    #return payment instance to poll_outgoing_transactions

    return ElinkPayment.objects.get(transaction=transaction)


def asset_create(request):
    import os
    from polaris.models import Asset

    asset_code = input('Enter Asset Name: ')
    asset_name = input('Enter Asset Code: ')
    asset_issuer = 'GCUNL4X72TO6D62UB6ABMJBFNWIJFTAJM6N3IGUNW6AFITTYQ4JWKPX6'
    asset_issuer_seed = 'SBHI3TDD7P73HD3ITPBFAMRA4H6QH5CIE4VCGSAPNRPTZFXGWKNAXFX2'
    asset_distributor_seed = 'SDOIHVVSLUDPKUYGTI2SFYIBLGWWFVFJYOHJC4Q6E4TNALDQU2F6BO4U'

    Asset.objects.create(
        code=asset_code,
        issuer=asset_issuer,
        distribution_seed=asset_distributor_seed,
        sep24_enabled=True,
        deposit_enabled=True,
        withdrawal_enabled=True,
        symbol=asset_name
    )


    os.system(f' cmd /k "python manage.py testnet issue --asset {asset_code} --issuer-seed {asset_issuer_seed} --distribution-seed {asset_distributor_seed}" ')
    return render('Done')