from uuid import uuid4

from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission

from polaris.models import Transaction, OffChainAsset


def get_new_token():
    return str(uuid4())

class MyElinkUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            # username = first_name + '_' + last_name,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    

class ElinkUser(AbstractBaseUser):
    """
    User/Customer account from the Elink Platform
    """
    
    first_name          = models.CharField(max_length=254)
    last_name           = models.CharField(max_length=254)
    email               = models.EmailField(unique=True)
    phone_number        = models.CharField(max_length=13)

    user_permissions = models.ManyToManyField(Permission)       #When you get 'ElinkUser' object has no attribute 'user_permissions' Error
    date_joined      = models.DateTimeField(auto_now_add=True)
    last_login       = models.DateTimeField(auto_now_add=True)
    is_admin         = models.BooleanField(default=False)  
    is_staff         = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=False)  
    is_superadmin    = models.BooleanField(default=False)  
    is_superuser     = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyElinkUserManager()

    @property
    def name(self):
        return " ".join([str(self.first_name), str(self.last_name)])

    def __str__(self):
        return f"{self.name} ({self.id})"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    def full_name(self):
        return (self.first_name + ' ' + self.last_name)


class ElinkPaymentProvider(models.Model):
    """
    
    """
    
    provider_name = models.CharField(max_length=50)


class ElinkUserKYC(models.Model):
    """
    To store additional information connected to a user.
    """

    user      = models.ForeignKey(ElinkUser, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=254)
    address_2 = models.CharField(max_length=254)
    country   = models.CharField(max_length=30)
    city      = models.CharField(max_length=50)
    state     = models.CharField(max_length=50)
    zip_code  = models.CharField(max_length=15)

    bvn              = models.CharField(max_length=11)
    payment_account  = models.CharField(max_length=10)
    payment_provider = models.ForeignKey(ElinkPaymentProvider, on_delete=models.CASCADE)


class ElinkCustodyAccount(models.Model):
    """
    
    """

    user             = models.ForeignKey(ElinkUser, on_delete=models.CASCADE)
    payment_provider = models.ForeignKey(ElinkPaymentProvider, on_delete=models.CASCADE)
    account_number   = models.CharField(max_length=10)
    active           = models.BooleanField(default=True)


class ElinkStellarAccount(models.Model):
    """
    Customer Account relation with Stellar
    """

    user               = models.OneToOneField(ElinkUser, on_delete=models.CASCADE)     #Change to one to one field
    memo               = models.TextField(null=True, blank=True)
    memo_type          = models.TextField(null=True, blank=True)
    account            = models.CharField(max_length=100)
    muxed_account      = models.TextField(null=True, blank=True)
    # secret_key         = models.CharField(max_length=100)
    confirmed          = models.BooleanField(default=False)
    confirmation_token = models.CharField(max_length=36, default=get_new_token)

    objects = models.Manager()

    class Meta:
        unique_together = ["memo", "account", "muxed_account"]

    def __str__(self):
        return f"{str(self.user)}: {str(self.muxed_account or self.account)} (memo: {str(self.memo)})"


class ElinkUserTransaction(models.Model):
    """
    Since we cannot add a ElinkStellarAccount foreign key to :class:`Transaction`,
    this table serves to join the two entities.
    """

    transaction_id        = models.TextField(db_index=True)
    user                  = models.ForeignKey(ElinkUser, on_delete=models.CASCADE, null=True)
    account               = models.ForeignKey(ElinkStellarAccount, on_delete=models.CASCADE, null=True)
    requires_confirmation = models.BooleanField(default=False)
    confirmed             = models.BooleanField(default=False)

    @property
    def transaction(self):
        return Transaction.objects.filter(id=self.transaction_id).first()

    objects = models.Manager()

    def __str__(self):
        return f"{str(self.account)}: {str(self.transaction)}"


class ElinkPayment(models.Model):
    """
    To track the completion of Withdraw Transactions.
    Works hand in hand with the Polaris Transaction Model.
    """

    choices = (
        ('DELIVERED', 'DELIVERED'),
        ('INITIALIZED', 'INITIALIZED'),
        ('FAILED', 'FAILED')
    )

    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    status      = models.CharField(max_length=20, choices=choices, default='INITIALIZED')


class ElinkFundingAccount(models.Model):
    """
    
    """

    user             = models.ForeignKey(ElinkUser, on_delete=models.CASCADE)
    payment_provider = models.ForeignKey(ElinkPaymentProvider, on_delete=models.CASCADE)
    account_number   = models.CharField(max_length=10)
    active           = models.BooleanField(default=True)

class OffChainAssetExtra(models.Model):
    """
    Extra information on off-chain assets that Elink' model doesn't store
    """

    offchain_asset = models.OneToOneField(OffChainAsset, primary_key=True, on_delete=models.CASCADE)
    fee_fixed      = models.DecimalField(default=0, max_digits=30, decimal_places=7)
    fee_percent    = models.PositiveIntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return f"OffChainAsset: {self.offchain_asset.asset_identification_format}"


class ElinkUserMonoTransaction(models.Model):
    user                 = models.ForeignKey(ElinkUser, on_delete=models.CASCADE)
    mono_trasaction_type = models.CharField(max_length=30)
    mono_account         = models.CharField(max_length=50)
    mono_amount          = models.IntegerField()
    mono_created_at      = models.CharField(max_length=50)
    mono_currency        = models.CharField(max_length=10)
    mono_customer        = models.CharField(max_length=50, blank=True, null=True)
    mono_description     = models.CharField(max_length=100)
    mono_fee             = models.IntegerField()
    mono_id              = models.CharField(max_length=50)
    mono_live_mode       = models.BooleanField()
    mono_reference       = models.CharField(max_length=50)
    mono_status          = models.CharField(max_length=20)
    mono_updated_at      = models.CharField(max_length=50)