from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Brewery
from .serializers import BrewerySerializer, UserSerializer
from .permissions import IsAdminOrReadOnly

class BreweryList(generics.ListCreateAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer

    permission_classes = (IsAdminOrReadOnly,)

class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer

    permission_classes = (IsAdminOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAdminUser,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAdminUser,)