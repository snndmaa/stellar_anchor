from typing import Dict, List
from polaris.integrations import DepositIntegration
from polaris.sep10.token import SEP10Token
from polaris.models import Transaction
from rest_framework.request import Request
from elink.views import user_for_account, calculate_fee
# from .rails import calculate_fee, memo_for_transaction

class AnchorDeposit(DepositIntegration):
    def process_sep6_request(
        self,
        token: SEP10Token,
        request: Request,
        params: Dict,
        transaction: Transaction,
        *args: List,
        **kwargs: Dict
    ) -> Dict:
        # check if the user's KYC has been approved
        kyc_fields = [
            "first_name",
            "last_name",
            "email_address",
            "address",
            "bank_account_number",
            "bank_number"
        ]

        # user = user_for_account(
        #     token.muxed_account or token.stellar_account
        # )
        user = user_for_account(token.account)

        # if not user or not user.kyc_approved:
        #     if user.kyc_rejected:
        #         return {
        #             "type": "customer_info_status",
        #             "status": "denied"
        #         }
        #     missing_fields = [
        #         field for field in kyc_fields
        #         if not getattr(user, field, None)
        #     ]
        #     if not missing_fields:
        #         return {
        #             "type": "customer_info_status",
        #             "status": "pending"
        #         }
        #     else:
        #         return {
        #             "type": "non_interactive_customer_info_needed",
        #             "fields": missing_fields
        #         }
        # user's KYC has been approved
        transaction.amount_fee = calculate_fee(transaction)
        # transaction.amount_out = round(
        #     transaction.amount_in - transaction.amount_fee,
        #     transaction.asset.significant_decimals
        # )
        # transaction.save()
        # user.add_transaction(transaction)
        return {
            "how": (
                "Make a wire transfer to the following account. "
                "Accounting Number: 94922545 ; Routing Number: 628524560. "
                "Users MUST include the following memo: "
                # f"{transaction_for_memo(transaction)}"
            ),
            "extra_info": {
                "accounting_number": "94922545",
                "routing_number": "628524560",
                # "memo": f"{transaction_for_memo(transaction)}",
            }
        }