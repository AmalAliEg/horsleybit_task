from django.urls import path
from .views import UserRawView, WalletRawView, TransactionRawView

urlpatterns = [
    #to add new users 
    path('users-raw/', UserRawView.as_view()),
    path('users-raw/<str:username>/', UserRawView.as_view()),
    path('wallets-raw/', WalletRawView.as_view()),
    path('transactions-raw/<int:pk>/', TransactionRawView.as_view()),
    path('transactions-raw/', TransactionRawView.as_view()),
]
