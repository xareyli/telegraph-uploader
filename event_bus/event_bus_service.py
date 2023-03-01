from event_bus.messages.bus_messages import BusMessage
import logging


class EventBusService:
    bus = {}

    def __init__(self):
        logging.info("Event Bus: bus system started")

    def subscribe(self, event: BusMessage, handler):
        logging.info("Event Bus: subscribing handler")

        if not (event.type in self.bus):
            self.bus[event.type] = []

        self.bus[event.type].append(handler)

    def unsubscribe(self, event, handler):
        logging.info("Event Bus: deleting handler")

        if not (event.type in self.bus):
            return

        subs = self.bus[event.type]

        self.bus[event.type] = [sub for sub in subs if sub != handler]

    def publish(self, event: BusMessage):
        logging.info("Event Bus: publishing message {}".format(event.type))

        for subscriber in self.bus[event.type]:
            subscriber(event)


bus_instance = EventBusService()
