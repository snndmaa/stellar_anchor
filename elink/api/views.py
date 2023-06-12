import requests
from polaris.models import Asset
from stellar_sdk import Server, exceptions as StellarError


from rest_framework import status, generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import StellarAssetSerializer, ElinkUserSerializer, ElinkStellarAccountSerializer, ElinkUserTransactionSerializer, ElinkUserMonoTransactionSerializer
from elink import models
# from elink import signal


class StellarAssetView(APIView):
    def get(self, request):
        queryset   = Asset.objects.all()
        serializer = StellarAssetSerializer(queryset, many=True)
        return Response(serializer.data)

class UserView(viewsets.ModelViewSet):
    queryset = models.ElinkUser.objects.all()
    serializer_class = ElinkUserSerializer
    # http_method_names = ['get', 'post', 'head']


# class AccountView(viewsets.ModelViewSet):
#     queryset = models.ElinkStellarAccount.objects.all()
#     serializer_class = ElinkStellarAccountSerializer
#     # http_method_names = ['get', 'post', 'head']

class AccountView(APIView):
    
    def get(self, request):
        queryset = models.ElinkStellarAccount.objects.all()
        serializer = ElinkStellarAccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = ElinkStellarAccountSerializer(data=request.data)

        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserTransactionView(viewsets.ModelViewSet):
    serializer_class = ElinkUserTransactionSerializer

    def get_queryset(self):
        return models.ElinkUserTransaction.objects.all()


# class UserMonoTransactionView(viewsets.ModelViewSet):
#     serializer_class = ElinkUserMonoTransactionSerializer

#     def get_queryset(self):
#         return models.ElinkUserMonoTransaction.objects.all()


class UserMonoTransactionView(APIView):
    
    def get(self, request):
        queryset   = models.ElinkUserMonoTransaction.objects.all()
        serializer = ElinkUserMonoTransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = ElinkUserMonoTransactionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['GET'])
def userbalancedetail(request, pk):
    server = Server("https://horizon-testnet.stellar.org")
    # instance = models.ElinkStellarAccount(user=request.user)
    instance = models.ElinkStellarAccount.objects.get(user_id=pk)

    try:
        account = server.accounts().account_id(f'{instance.account}').call()
        for balance in account['balances']:
            return Response({'Type': balance['asset_type'], 'Balance': balance['balance']})
    except models.ElinkStellarAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except StellarError.NotFoundError:
        try:
            response = requests.get(f"https://friendbot.stellar.org?addr={instance.account}")
            account = server.accounts().account_id(f'{instance.account}').call()
            for balance in account['balances']:
                return Response({'Type': balance['asset_type'], 'Balance': balance['balance']})
        except:
            return Response(status=status.HTTP_402_PAYMENT_REQUIRED)