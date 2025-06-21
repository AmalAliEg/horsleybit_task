# ---------- 4) app2/urls.py (Router DRF) ----------
from rest_framework.routers import DefaultRouter
from .views import WalletViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r"wallets", WalletViewSet, basename="wallet")
router.register(r"transactions", TransactionViewSet, basename="transaction")

urlpatterns = router.urls   # ← يُصدِّر المسارات الجاهزة

# مثال للمسارات التي يولدها:
# /wallets/           → list  + create
# /wallets/<pk>/      → retrieve + update + destroy
# /transactions/      → list  + create
# /transactions/<pk>/ → retrieve + update + destroy