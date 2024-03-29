from email.mime import base
from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', views.UserView, basename='users')
# router.register('accounts', views.AccountView, basename='accounts')
router.register('usertransaction', views.UserTransactionView, basename='usertransaction')


urlpatterns = [
    path('', include(router.urls)),
    path('assets', views.StellarAssetView.as_view(), name='assets'),
    path('accounts', views.AccountView.as_view(), name='accounts'),
    path('account/<int:pk>', views.AccountView, name='account'),
    path('monouser', views.UserMonoTransactionView.as_view(), name='monouser'),
    path('balance/<int:pk>/', views.userbalancedetail, name='user_balance')
]
