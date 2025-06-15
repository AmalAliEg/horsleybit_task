from django.contrib import admin


from .models import Users_db
# Register your models here.
#here where i can give the admin ability the edit over the homepage


admin.site.register(Users_db)
