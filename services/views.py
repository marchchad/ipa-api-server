from django.contrib.auth.models import User, Group
from django.contrib import admin

from services.permissions import IsOwnerOrReadOnly, IsOwnerFilterBackend

admin.autodiscover()

from rest_framework import viewsets, generics, permissions, filters
from serializers import UserSerializer, GroupSerializer, KegSerializer, RecipeSerializer

from models import Keg, Recipe


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAdminUser,)


class KegViewset(viewsets.ModelViewSet):
    queryset = Keg.objects.all()
    serializer_class = KegSerializer
    filter_backends = (IsOwnerFilterBackend,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (IsOwnerFilterBackend,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
