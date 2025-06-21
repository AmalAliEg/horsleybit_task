# ---------- 1) app2/models.py ----------
from django.db import models

class Wallet(models.Model):
    id       = models.BigAutoField(primary_key=True)
    user_id  = models.IntegerField()
    currency = models.CharField(max_length=10)
    balance  = models.DecimalField(max_digits=24, decimal_places=8)

    class Meta:
        managed   = False           # ← الجداول موجودة مُسبقًا
        db_table  = "wallet_table"  # ← اسم الجدول الحقيقي فى DB
        app_label = "app2"          # ← يربط الموديل بالتطبيق


class Transaction(models.Model):
    id               = models.BigAutoField(primary_key=True)
    transaction_hash = models.CharField(max_length=64, unique=True)
    sender_user_id   = models.IntegerField()
    receiver_user_id = models.IntegerField()
    amount           = models.DecimalField(max_digits=24, decimal_places=8)
    status           = models.CharField(max_length=20)

    class Meta:
        managed   = False
        db_table  = "transaction_table"
        app_label = "app2"