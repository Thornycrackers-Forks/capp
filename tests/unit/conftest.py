"""Fixtures used for tests."""

from pytest_factoryboy import register

from tests import factories

register(factories.UserFactory)
register(factories.SuperUserFactory)
register(factories.TalkFactory)
