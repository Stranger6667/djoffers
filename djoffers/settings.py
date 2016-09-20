# coding: utf-8
from django.conf import settings


DEFAULT_CONFIG = {
    'ENDPOINT': 'https://api.hasoffers.com/Apiv3/json',
    'NETWORK_TOKEN': None,
    'NETWORK_ID': None,
    'VERIFY': True,
    'RETRIES': 3,
    'RETRY_TIMEOUT': 3,
    'VERBOSITY': 0,
}
config = getattr(settings, 'HASOFFERS', DEFAULT_CONFIG)


def get_value(key):
    return config.get(key, DEFAULT_CONFIG[key])

ENDPOINT = get_value('ENDPOINT')
NETWORK_TOKEN = get_value('NETWORK_TOKEN')
NETWORK_ID = get_value('NETWORK_ID')
VERIFY = get_value('VERIFY')
RETRIES = get_value('RETRIES')
RETRY_TIMEOUT = get_value('RETRY_TIMEOUT')
VERBOSITY = get_value('VERBOSITY')
