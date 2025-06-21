from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()


class WalletSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    currency = serializers.CharField(max_length=10)
    balance = serializers.DecimalField(max_digits=24, decimal_places=8)


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    transaction_hash = serializers.CharField(max_length=64)
    sender_user_id = serializers.IntegerField()
    receiver_user_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=24, decimal_places=8)
    status = serializers.CharField(max_length=20)

    def validate_status(self, value):
        allowed = {"pending", "completed", "failed"}
        if value not in allowed:
            raise serializers.ValidationError("Invalid status value")
        return value