from event_bus import bus_instance, bus_messages
from utils import save_token_to_file
from store import store
import logging


def onTokenCreated(event):
    logging.info('APP: writing access token to a file')
    save_token_to_file(store.dget('API', 'access_token'))

bus_instance.subscribe(bus_messages.TokenCreationDoneEvent(), onTokenCreated)
