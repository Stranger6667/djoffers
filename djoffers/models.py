# coding: utf-8
from django.db import models
from django.utils.decorators import classproperty

from pyoffers.api import HasOffersAPI

from .settings import ENDPOINT, NETWORK_TOKEN, NETWORK_ID, VERIFY, RETRIES, RETRY_TIMEOUT, VERBOSITY


class HasOffersModel(models.Model):
    """
    Basic entity to store on our side. It points to remote HasOffers entity via integer ID.
    """
    hasoffers_id = models.IntegerField(unique=True)

    hasoffers = HasOffersAPI(
        endpoint=ENDPOINT,
        network_token=NETWORK_TOKEN,
        network_id=NETWORK_ID,
        verify=VERIFY,
        retries=RETRIES,
        retry_timeout=RETRY_TIMEOUT,
        verbosity=VERBOSITY,
    )

    class Meta:
        abstract = True

    @classproperty
    def manager_name(self):
        return self.__name__

    @property
    def instance(self):
        """
        Convenience wrapper for remote instance. Taken from `pyoffers`.
        """
        return self.manager.find_by_id(self.hasoffers_id)

    @property
    def manager(self):
        return self.hasoffers._managers[self.manager_name]
