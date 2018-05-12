# coding: utf-8
from pyoffers.models import OfferManager

from .app.models import Offer


def test_smoke():
    from djoffers.settings import config  # noqa


def test_manager_name():
    assert Offer.manager_name == 'Offer'


def test_manager():
    assert isinstance(Offer().manager, OfferManager)
