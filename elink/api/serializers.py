from rest_framework import serializers
from elink.models import ElinkUser, ElinkStellarAccount, ElinkUserTransaction


class ElinkUserTransactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    account = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ElinkUserTransaction
        fields = "__all__"


class ElinkStellarAccountSerializer(serializers.ModelSerializer):
    transaction = ElinkUserTransactionSerializer(many=True, read_only=True)
    # user = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = ElinkStellarAccount
        fields = "__all__"


class ElinkUserSerializer(serializers.ModelSerializer):
    transaction = ElinkUserTransactionSerializer(many=True, read_only=True)
    account = ElinkStellarAccountSerializer(many=True, read_only=True)

    class Meta:
        model = ElinkUser
        fields = "__all__"