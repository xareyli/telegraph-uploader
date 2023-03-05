from event_bus import bus_instance, bus_messages
from utils import save_token_to_file, export_token_from_file
from store import store
import logging


def on_token_created(event):
    logging.info('APP: writing access token to a file')
    save_token_to_file(store.dget('API', 'access_token'))

bus_instance.subscribe(bus_messages.TokenCreationDoneEvent(), on_token_created)


def on_app_started():
    token = export_token_from_file()

    if token:
        store.dset('API', 'access_token', token)
        bus_instance.publish(bus_messages.SetSavedTokenEvent())
