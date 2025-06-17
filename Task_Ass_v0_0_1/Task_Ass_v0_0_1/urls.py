from django.contrib import admin
from django.urls import path
from Users.views import UserListCreate, UserDelete
from Users import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_root, name='api-root'),  # Add this
    path('api/users/', UserListCreate.as_view(), name='users-list'),
    path('api/users/<int:pk>/', UserDelete.as_view(), name='user-detail'),
]