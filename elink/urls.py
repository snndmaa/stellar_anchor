from django.urls import path
from .views import asset_create

urlpatterns = [
    path('create_asset', asset_create, name='asset_create'),
]