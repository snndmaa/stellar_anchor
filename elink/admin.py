from django.contrib import admin
from .models import ElinkUser, ElinkStellarAccount, ElinkUserTransaction, ElinkUserKYC, ElinkPayment, ElinkCustodyAccount, ElinkFundingAccount, ElinkPaymentProvider

# Register your models here.
admin.site.register(ElinkUser)
admin.site.register(ElinkStellarAccount)
admin.site.register(ElinkUserTransaction)
admin.site.register(ElinkUserKYC)
admin.site.register(ElinkPayment)
admin.site.register(ElinkCustodyAccount)
admin.site.register(ElinkFundingAccount)
admin.site.register(ElinkPaymentProvider)