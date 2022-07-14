from rest_framework.request import Request
from polaris.models import Asset

def return_toml_contents(request, *args, **kwargs):
    asset = Asset.objects.first()
    return {
        'DOCUMENTATION': {
            'ORG_NAME': 'Test Organisation',
            'ORG_URL': '',
            'ORG_LOGO': '',
            'ORG_DESCRIPTION': 'Test Description',
            'ORG_OFFICIAL_EMAIL': 'test@test.com',
            'ORG_SUPPORT_EMAIL': ''
        },
        'CURRENCIES': [
            {
                'code': asset.code,
                'issuer': asset.issuer,
                'status': 'test',
                'display_decimals': 2,
                'name': 'Test Currency',
                'desc': 'A fake asset on the testnet for demo purposes'
            }
        ]
    }