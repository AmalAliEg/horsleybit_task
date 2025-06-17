from rest_framework import generics
from .models import Users_db
from .serializers import UserSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
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
    serializer_class = UserSerializer

class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users_db.objects.all()
    serializer_class = UserSerializer