# coding: utf-8
from django.conf import settings


DEFAULT_CONFIG = {
    'ENDPOINT': 'https://api.hasoffers.com/Apiv3/json',
    'NETWORK_TOKEN': None,
    'NETWORK_ID': None,
    'VERIFY': True,
    'VERBOSITY': 0,
}
config = getattr(settings, 'HASOFFERS', DEFAULT_CONFIG)

ENDPOINT = config.get('ENDPOINT', DEFAULT_CONFIG['ENDPOINT'])
NETWORK_TOKEN = config.get('NETWORK_TOKEN', DEFAULT_CONFIG['NETWORK_TOKEN'])
NETWORK_ID = config.get('NETWORK_ID', DEFAULT_CONFIG['NETWORK_ID'])
VERIFY = config.get('VERIFY', DEFAULT_CONFIG['VERIFY'])
VERBOSITY = config.get('VERBOSITY', DEFAULT_CONFIG['VERBOSITY'])
