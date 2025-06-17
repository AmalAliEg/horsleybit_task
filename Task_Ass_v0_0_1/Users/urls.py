from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root.as_view(), name='api-root'), 
    path('api/users/', views.UserListCreate.as_view(), name='users-list'),
    path('api/users/<int:pk>/', views.UserDelete.as_view(), name='user-detail'),
]