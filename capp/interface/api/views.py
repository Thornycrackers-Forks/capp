"""Core Views."""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import viewsets

from data import models

from . import serializers

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class TalkViewSet(viewsets.ModelViewSet):
    """API endpoint that allows talks to be viewed or edited."""

    queryset = models.Talk.objects.all()
    serializer_class = serializers.TalkSerializer
