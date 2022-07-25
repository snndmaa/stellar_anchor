from typing import Optional
from decimal import Decimal
from django import forms
from rest_framework.request import Request
from polaris.models import Transaction
from polaris.templates import Template
from polaris.integrations import (
    DepositIntegration,
    # WithdrawIntegration,
    TransactionForm
)
from .forms import ContactForm, KYCForm, BankAccount
from elink.models import ElinkUserKYC
from elink.views import user_for_account, create_user, update_user_kyc

class AnchorDeposit(DepositIntegration):
    def form_for_transaction(
        self,
        request: Request,
        transaction: Transaction,
        post_data: dict = None,
        amount: Decimal = None,
        *args,
        **kwargs
    ):
        # if we haven't collected amount, collect it
        if not transaction.amount_in:
            if post_data:
                return TransactionForm(transaction, post_data)
            else:
                return TransactionForm(transaction, initial={"amount": amount})

        # if a user doesn't exist for this Stellar account,
        # collect their contact info
        user = user_for_account(
            transaction.muxed_account or transaction.stellar_account
        )
        kyc_info = ElinkUserKYC.objects.filter(user=user)

        if not user:
            if post_data:
                return ContactForm(post_data)
            else:
                return ContactForm()
        # if we haven't gotten the user's full address, collect it            
        elif not kyc_info:
            if post_data:
                return KYCForm(post_data)
            else:
                return KYCForm()
        # we don't have anything more to collect
        else:
            return None

    def after_form_validation(
        self,
        request: Request,
        form: forms.Form,
        transaction: Transaction,
        *args,
        **kwargs,
    ):

        if isinstance(form, TransactionForm):
            # Polaris automatically assigns amount to Transaction.amount_in
            return
        if isinstance(form, ContactForm):
            # creates the user to be returned from user_for_account()
            create_user(form)
        elif isinstance(form, KYCForm):
            # assigns user.full_address
            # print(form.cleaned_data['state'])
            update_user_kyc(form, user_for_account(transaction.stellar_account))
            return

    def content_for_template(
        self,
        request: Request,
        template: Template,
        form: Optional[forms.Form] = None,
        transaction: Optional[Transaction] = None,
        *args,
        **kwargs,
    ):
        if form is not None or template == Template.MORE_INFO:
            # provides a label for the image displayed at the top of each page
            return {"icon_label": "Elink Markets."}
        else:
            # we're done
            return None