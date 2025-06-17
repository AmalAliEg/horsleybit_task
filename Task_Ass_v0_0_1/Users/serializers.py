from rest_framework import serializers
from .models import Users_db

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_db
        fields = '__all__'