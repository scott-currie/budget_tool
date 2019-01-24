from rest_framework import generics
from .serializers import UserSerializer, User
from rest_framework.authentication import TokenAuthentication


class UserApiView(generics.RetrieveAPIView):
    """CBV to handle requests for users on REST API.

    """
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class RegisterApiView(generics.CreateAPIView):
    """CBV to handle registration requests on REST API.

    """
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer
