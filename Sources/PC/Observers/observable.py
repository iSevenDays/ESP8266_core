from Sources.Shared.Logger import Logger


class Observable(object):
    def __init__(self):
        self.observers = []
        self.logger = Logger.Logger(self.__class__.__name__)
        self.logger.debug("init ")

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            self.logger.debug("added observer: %s", observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def notify(self, data):
        self.logger.debug("notified %s", self.observers)
        for observer in self.observers:
            observer.on_received_data(data)


