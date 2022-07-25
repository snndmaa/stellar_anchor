from django import forms
from elink.models import ElinkUserKYC
#ADD SPECIFICATIONS TO FIELDS

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name  = forms.CharField()
    email      = forms.EmailField()


class KYCForm(forms.ModelForm):
    class Meta:
        model = ElinkUserKYC
        exclude = ('user',)


class BankAccount(forms.Form):
    account_number = forms.CharField()
    routing_number = forms.CharField()
    bvn = forms.CharField()
