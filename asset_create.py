import os
from polaris.models import Asset

asset_code = input('Enter Asset Code: ')
asset_symbol = input('Enter Asset Symbol: ')
asset_issuer = 'GA2RUSQQYQTZJRXRUJRR6OFJ3Q3O7XUU27ZOFYIBHUK3D656RW6WQT5C'
asset_distributor_seed = 'SAJ266DP3MJTOAFLWCJ7BONGX4MASUMDOUWBNVR3TQ7F3SYGQUY3IRAT'

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