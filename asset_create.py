import os
from polaris.models import Asset

asset_code = input('Enter Asset Code: ')
asset_symbol = input('Enter Asset Symbol: ')
asset_issuer = 'GCUNL4X72TO6D62UB6ABMJBFNWIJFTAJM6N3IGUNW6AFITTYQ4JWKPX6'
asset_issuer_seed = 'SBHI3TDD7P73HD3ITPBFAMRA4H6QH5CIE4VCGSAPNRPTZFXGWKNAXFX2'
asset_distributor_seed = 'SDOIHVVSLUDPKUYGTI2SFYIBLGWWFVFJYOHJC4Q6E4TNALDQU2F6BO4U'

Asset.objects.create(
    code=asset_code,
    issuer=asset_issuer,
    distribution_seed=asset_distributor_seed,
    sep24_enabled=True,
    deposit_enabled=True,
    withdrawal_enabled=True,
    symbol=asset_symbol
)


# os.system(f' cmd /k "python manage.py testnet issue --asset {asset_code} --issuer-seed {asset_issuer_seed} --distribution-seed {asset_distributor_seed}" ')

# python manage.py testnet issue --asset TEST --issuer-seed <...> --distribution-seed <...>