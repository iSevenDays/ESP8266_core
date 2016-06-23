import socketserver

from Sources.PC.PCSocketConnection import PCSocketConnection
from Sources.PC.Observers.observable import Observable
from Sources.Shared.Logger import Logger


class PCServer(Observable):
    HOST, PORT = '', 9999

    def __init__(self):
        super().__init__()
        self.logger = Logger.Logger(self.__class__.__name__)
        self.server = socketserver.TCPServer((self.HOST, self.PORT), PCSocketConnection)

    def serve_forever(self):
        # Create the server, binding to localhost on port 9999
        self.server.pc_server = self
        if self.HOST:
            self.logger.info("Server %s started, host <%s> port: %d", self.server, self.HOST, self.PORT)
        else:
            self.logger.info("Server %s started at localhost, port: %d", self.server, self.PORT)
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        self.server.serve_forever()

    def on_received_connection_data(self, ip_address, data):
        self.logger.debug(self, "on_received_connection_data, data: %s from ip: %s", data, ip_address)
        self.notify(data)
