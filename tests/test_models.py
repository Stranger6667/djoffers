# coding: utf-8
from .app.models import Offer


def test_smoke():
    from djoffers.settings import config


def test_manager_name():
    assert Offer.manager_name == 'Offer'
