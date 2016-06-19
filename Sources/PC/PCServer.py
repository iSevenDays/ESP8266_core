import socketserver


class PCServer(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.data = self.request.recv(1024).strip()

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


if __name__ == "__main__":
    HOST, PORT = '', 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), PCServer)

    print("Started: %s   Port: %d" % (HOST, PORT))
    print("Server: ", server)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
