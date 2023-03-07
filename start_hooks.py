from event_bus import bus_instance, bus_messages
from utils import save_token_to_file, export_token_from_file
from store import store
import logging
from os.path import abspath
import os


def on_token_created(event):
    logging.info('APP: writing access token to a file')
    save_token_to_file(store.dget('API', 'access_token'))

bus_instance.subscribe(bus_messages.TokenCreationDoneEvent(), on_token_created)


def load_token_from_file():
    token = export_token_from_file()

    if token:
        store.dset('API', 'access_token', token)
        bus_instance.publish(bus_messages.SetSavedTokenEvent())


def clearLogs():
    if len([name for name in os.listdir(abspath('./logs'))]) > 7:
        for path,subdir,files in os.walk(abspath('./logs')):
            for name in files:
                fullpath = os.path.join(path,name)

                try:
                    os.remove(fullpath)
                except:
                    continue


def on_app_started():
    load_token_from_file()
    clearLogs()
