from rest_framework import viewsets
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset         = Wallet.objects.using("default").all()
    serializer_class = WalletSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset         = Transaction.objects.using("default").all()
    serializer_class = TransactionSerializer