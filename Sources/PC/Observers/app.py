from Sources.PC.Observers.observer import Observer
from Sources.PC.PCServer import PCServer
from Sources.Shared.Logger import Logger


class MyPlayer(Observer):
    def __init__(self):
        self.logger = Logger.Logger(self.__class__.__name__)

    def on_received_data(self, data):
        self.logger.debug("received data: %s", data)


if __name__ == "__main__":
    pcServer = PCServer()
    myplayer = MyPlayer()

    pcServer.register(myplayer)

    pcServer.serve_forever()
