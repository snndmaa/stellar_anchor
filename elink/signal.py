from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from stellar_sdk import Keypair

from .models import ElinkStellarAccount


@receiver(post_save, sender=settings.AUTH_USER_MODEL)       #post_save is a signal used to perform an action after the object in the sender is saved
def create_user_account(sender, instance=None, created=False, **kwargs):
    if created:
        pair = Keypair.random()
        stellar_account = ElinkStellarAccount(
                                user=instance,
                                account=pair.public_key,
                                secret_key=pair.secret
                            )         #instance is initially None and then after the user is created a signal(called create_auth_token) is fired which creates a Token instance with a foreign key pointing to the instance of the user.
        stellar_account.save()
        
        # response = requests.get(f"https://friendbot.stellar.org?addr={pair.public_key}")