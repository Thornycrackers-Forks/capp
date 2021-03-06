"""Test serializers."""
from typing import Dict

from django.test.client import Client

import pytest
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from data import models
from interface.api import serializers
from tests import factories


@pytest.fixture
def context() -> Dict:
    """Hyperlinked serializers require a context."""
    factory = APIRequestFactory()
    request = factory.get("/")
    context = {"request": Request(request)}
    return context


@pytest.mark.django_db
def test_get_all_talks(client: Client, talk_factory: factories.TalkFactory) -> None:
    """Test serializer returns talks."""
    talk_factory(name="One")
    talk_factory(name="Two")
    talk_factory(name="Three")
    response = client.get("/api/talks/")
    talks = models.Talk.objects.all()
    serializer = serializers.TalkSerializer(talks, many=True)
    response.data == serializer.data
    response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_all_speakers(
    client: Client, speaker_factory: factories.SpeakerFactory, context: Dict
) -> None:
    """Test serializer returns talks."""
    speaker_factory()
    speaker_factory()
    speaker_factory()
    response = client.get("/api/speakers/")
    speakers = models.Speaker.objects.all()
    serializer = serializers.SpeakerSerializer(speakers, many=True, context=context)
    response.data == serializer.data
    response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_all_categories(
    client: Client, category_factory: factories.CategoryFactory
) -> None:
    """Test serializer returns categories."""
    category_factory(name="One")
    category_factory(name="Two")
    category_factory(name="Three")
    response = client.get("/api/categories/")
    categories = models.Category.objects.all()
    serializer = serializers.CategorySerializer(categories, many=True)
    response.data == serializer.data
    response.status_code == status.HTTP_200_OK
