from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    transaction_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Transaction
        fields = ['transaction_id', 'amount', 'transaction_type', 'timestamp', 'status', 'user']
