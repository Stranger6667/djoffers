# coding: utf-8
from django.db import models

from pyoffers.api import HasOffersAPI

from .settings import ENDPOINT, NETWORK_TOKEN, NETWORK_ID, VERIFY, VERBOSITY


class HasOffersModel(models.Model):
    """
    Basic entity to store on our side. It points to remote HasOffers entity via integer ID.
    """
    hasoffers_id = models.IntegerField(db_index=True)

    hasoffers = HasOffersAPI(ENDPOINT, NETWORK_TOKEN, NETWORK_ID, VERIFY, VERBOSITY)

    class Meta:
        abstract = True

    @property
    def instance(self):
        """
        Convenience wrapper for remote instance. Taken from `pyoffers`.
        """
        return self.hasoffers._managers[self.__class__.__name__].find_by_id(self.hasoffers_id)
