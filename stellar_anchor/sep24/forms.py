from django import forms
#ADD SPECIFICATIONS TO FIELDS

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name  = forms.CharField()
    email      = forms.EmailField()


class AddressForm(forms.Form):
    address_1 = forms.CharField()
    address_2 = forms.CharField()
    country   = forms.CharField()
    city      = forms.CharField()
    state     = forms.CharField()
    zip_code  = forms.CharField()


class BankAccount(forms.Form):
    account_number = forms.CharField()
    routing_number = forms.CharField()
