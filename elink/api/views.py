from requests import Response
from .serializers import ElinkUserSerializer, ElinkStellarAccountSerializer, ElinkUserTransactionSerializer
from rest_framework import status, generics, mixins, viewsets
from rest_framework.views import APIView
from elink import models
from rest_framework.response import Response


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

        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserTransactionView(viewsets.ModelViewSet):
    serializer_class = ElinkUserTransactionSerializer

    def get_queryset(self):
        return models.ElinkUserTransaction.objects.all()
    