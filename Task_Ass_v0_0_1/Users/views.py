from rest_framework import generics
from .models import Users_db
#Serializers convert between Django models and JSON/Python datatypes
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


#decorator converts a regular function into an API view
@api_view(['GET'])
#function that handles requests to the API root
def api_root(request):

    return Response({
        'message': 'Welcome to Users API',
        'endpoints': {
            'users': request.build_absolute_uri('/api/users/'),
            'user_detail': request.build_absolute_uri('/api/users/<id>/')
        }
    })
class UserListCreate(generics.ListCreateAPIView):
    queryset = Users_db.objects.all()
    #Used for both serializing (model-->JSON) and deserializing (JSON-->model)
    serializer_class = UserSerializer

class UserDelete(generics.DestroyAPIView):
    queryset = Users_db.objects.all()
    serializer_class = UserSerializer