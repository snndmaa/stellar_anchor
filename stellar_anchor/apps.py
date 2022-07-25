from django.apps import AppConfig


class AnchorConfig(AppConfig):
    name = 'stellar_anchor'

    def ready(self):
        from polaris.integrations import register_integrations
        from .sep1 import return_toml_contents
        # from .deposit import AnchorDeposit
        from .depositS6 import AnchorDeposit
        from .rails import AnchorRails
        from .customer import AnchorCustomer
        from .sep6.info import info

        register_integrations(
            toml=return_toml_contents,
            deposit=AnchorDeposit(),
            rails=AnchorRails(),
            customer=AnchorCustomer(),
            sep6_info=info,
        )