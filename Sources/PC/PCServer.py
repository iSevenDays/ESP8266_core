import socketserver
from Sources.PC.Observers.observable import Observable


class PCSocketConnection(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def __init__(self, request, client_address, server):
        self.pc_server = server.pc_server
        self.data = request.recv(1024).strip()
        super().__init__(request, client_address, server)

    def handle(self):
        # self.request is the TCP socket connected to the client
        # print "{} wrote:".format(self.client_address[0])
        print("ClientIP:", self.client_address[0])
        print("Rx: ", self.data)
        # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())
        reply = bytes(self.data).decode(encoding='UTF-8').upper()
        print("Tx: ", reply)
        self.request.sendall(str.encode(reply, 'UTF-8'))

        print("PCSocketConnection handle, data: ", self.data)
        print("PCServer: ", self.pc_server)
        self.pc_server.on_received_connection_data("", self.data)


class PCServer(Observable):
    HOST, PORT = '', 9999

    def __init__(self):
        super().__init__()
        self.server = socketserver.TCPServer((self.HOST, self.PORT), PCSocketConnection)

    def serve_forever(self):
        # Create the server, binding to localhost on port 9999
        self.server.pc_server = self

        print("Started: %s   Port: %d" % (self.HOST, self.PORT))
        print("Server: ", self.server)

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        self.server.serve_forever()

    def on_received_connection_data(self, ip_address, data):
        print(self, "on_received_connection_data, data: ", data)
        self.notify(data)
