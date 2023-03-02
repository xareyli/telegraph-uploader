from auth.view import AuthWindow
from event_bus import bus_instance, bus_messages

__all__ = [
    'auth_window'
]

auth_window = AuthWindow()

def onCreateToken(event):
    auth_window.show()

bus_instance.subscribe(bus_messages.CreateTokenCommand(), onCreateToken)
