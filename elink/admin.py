from django.contrib import admin
from .models import ElinkUser, ElinkStellarAccount, ElinkUserTransaction

# Register your models here.
admin.site.register(ElinkUser)
admin.site.register(ElinkStellarAccount)
admin.site.register(ElinkUserTransaction)