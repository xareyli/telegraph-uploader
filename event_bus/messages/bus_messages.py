class BusMessage:
    type = ''


# With a command component can initiate action
class _BaseCommand(BusMessage):
    def __init__(self, payload=None):
        self.payload = payload

# Event notifies about something is happened
class _BaseEvent(BusMessage):
    def __init__(self, payload=None):
        self.payload = payload

# --------------
# |  Commands  |
# --------------

class CreateTokenCommand(_BaseCommand):
    type = "create_token_command"

class ChooseFolderCommand(_BaseCommand):
    type = "choose_folder_command"

class UploadCommand(_BaseCommand):
    type = "upload_command"


# ------------
# |  Events  |
# ------------

class TokenCreationDoneEvent(_BaseEvent):
    type = "token_creation_done_event"

class FolderPickingDoneEvent(_BaseEvent):
    type = "folder_picking_done_event"

class UploadDoneEvent(_BaseEvent):
    type = "upload_done_event"

class TokenCreationFailedEvent(_BaseEvent):
    type = "token_creation_failed_event"
