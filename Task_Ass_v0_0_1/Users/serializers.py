from rest_framework import serializers
from .models import Users_db

class UserSerializer(serializers.ModelSerializer):
    #Inner class that provides metadata to the serializer
    class Meta:
        #which Django model to use
        model = Users_db
        fields = ['id', 'username','Phone_num', 'email', 'Gender','birthday']


