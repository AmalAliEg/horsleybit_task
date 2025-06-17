from django.contrib import admin
from django.urls import path,include
from Users.views import UserListCreate, UserDelete
from Users import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # Include app URLs
    path('', include('Users.urls')),  
]