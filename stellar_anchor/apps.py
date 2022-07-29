from django.apps import AppConfig


class AnchorConfig(AppConfig):
    name = 'stellar_anchor'

    def ready(self):
        from polaris.integrations import register_integrations
        from .sep1 import return_toml_contents
        # from .deposit import AnchorDeposit
        from .depositS6 import AnchorDeposit
        from .withdrawS6 import AnchorWithdrawal
        from .rails import AnchorRails
        from .customer import AnchorCustomer
        from .sep6.info import info
        from .process_sep6 import process_sep6_request

        register_integrations(
            toml=return_toml_contents,
            deposit=AnchorDeposit(),
            rails=AnchorRails(),
            customer=AnchorCustomer(),
            sep6_info=info,
            withdrawal=AnchorWithdrawal()
        )