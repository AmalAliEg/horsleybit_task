from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, WalletSerializer,TransactionSerializer

from .db_operations import (
    get_user_by_username,
    get_wallet,
    fetch_transaction,
    create_transaction,
    create_user,
    create_wallet
)

class UserRawView(APIView):
    """GET /users-raw/<username>/ – يعيد بيانات المستخدم بالـ raw SQL."""

    def get(self, request, username=str):
        user = get_user_by_username(username)
        if user is None:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(UserSerializer(user).data)
    
    def post(self, request):
        ser = UserSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=400)
        new_id = create_user(**ser.validated_data)
        return Response({'id': new_id}, status=201)



class WalletRawView(APIView):
    """GET /wallets-raw/?user_id=<int>&currency=<str> – محفظة واحدة."""

    def get(self, request):
        user_id = request.query_params.get('user_id')
        currency = request.query_params.get('currency')
        if not user_id or not currency:
            return Response({'detail': 'user_id & currency are required'}, status=status.HTTP_400_BAD_REQUEST)
        wallet = get_wallet(int(user_id), currency)
        if wallet is None:
            return Response({'detail': 'Wallet not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(WalletSerializer(wallet).data)


    def post(self, request):
        #convert data from client to serializer object
        ser=WalletSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=400)
        new_id = create_wallet(**ser.validated_data)
        return Response({'id': new_id}, status=201)


class TransactionRawView(APIView):
    """/transactions-raw/ – GET بالـ id أو POST إنشاء جديد."""

    def get(self, request, pk: int):
        TX = fetch_transaction(pk)
        if TX is None:
            return Response({'detail': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(TransactionSerializer(TX).data)

    def post(self, request):
        ser=TransactionSerializer(data=request.data)
        

        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

        new_id = create_transaction(
            tx_hash=ser.validated_data['transaction_hash'],
            sender_id=ser.validated_data['sender_user_id'],
            receiver_id=ser.validated_data['receiver_user_id'],
            amount=ser.validated_data['amount'],
        )

        return Response({'id': new_id}, status=status.HTTP_201_CREATED)
