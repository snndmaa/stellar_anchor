from typing import Dict, List
from polaris.integrations import CustomerIntegration
from polaris.sep10.token import SEP10Token
from polaris.models import Transaction
from rest_framework.request import Request
from elink.views import user_for_account

class AnchorCustomer(CustomerIntegration):
    def get(
        self,
        token: SEP10Token,
        request: Request,
        params: Dict,
        *args: List,
        **kwargs: Dict
    ) -> Dict:
        # user = user_for_account(
        #     token.muxed_account or token.account,
        #     token.memo or params.get("memo"),
        #     "id" if token.memo else params.get("memo_type")
        # )
        user = user_for_account(token.account)
        # fields = fields_for_type(params.get("type"))
        # if not user:
        #     return {
        #         "status": "NEEDS_INFO",
        #         "fields": fields
        #     }
        # missing_fields = dict([
        #     (f, v) for f, v in fields.items()
        #     if not getattr(user, f, False)
        # ])
        # provided_fields = dict([
        #     (f, v) for f, v in fields.items()
        #     if getattr(user, f, False)
        # ])
        # if missing_fields:
        #     return {
        #         "id": user.id,
        #         "status": "NEEDS_INFO",
        #         "fields": missing_fields,
        #         "provided_fields": provided_fields
        #     }
        if user:
            return {
                "DONE": "DONE"
            }
        else:
            return {
                "ERROR": "ERROR"
            }
        if user.rejected:
            return {
                "id": user.id,
                "status": "REJECTED",
                "provided_fields": provided_fields
            }
        if user.kyc_approved:
            return {
                "id": user.id,
                "status": "APPROVED",
                "provided_fields": provided_fields
            }
        # return {
        #     "id": user.id,
        #     "status": "PENDING",
        #     "provided_fields": provided_fields