from django.contrib import admin
from .models import ElinkUser, ElinkStellarAccount, ElinkUserTransaction, ElinkUserKYC

# Register your models here.
admin.site.register(ElinkUser)
admin.site.register(ElinkStellarAccount)
admin.site.register(ElinkUserTransaction)
admin.site.register(ElinkUserKYC)