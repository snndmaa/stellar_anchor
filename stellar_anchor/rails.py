from typing import List, Dict
from django.db.models import QuerySet
from polaris.models import Transaction
from polaris.integrations import RailsIntegration
# from .rails import (
#     get_reference_id,
#     has_received_payment
# )

class AnchorRails(RailsIntegration):
    def poll_pending_deposits(
        self,
        pending_deposits: QuerySet,
        *args: List,
        **kwargs: Dict
    ):
        # received_payments = []
        # for transaction in pending_deposits:
        #     if has_received_payment(get_reference_id(transaction)):
        #         received_payments.append(transaction)
        # return received_payments

        return list(pending_deposits)