from django.contrib import admin
from django.urls import path
from Users.views import UserListCreate, UserRetrieveUpdateDelete
from Users import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_root, name='api-root'),  # Add this
    path('api/users/', UserListCreate.as_view(), name='users-list'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name='user-detail'),
]