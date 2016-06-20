from Sources.PC.Observers.observer import Observer
from Sources.PC.PCServer import PCServer


class MyPlayer(Observer):
    def __init__(self):
        pass

    def on_received_data(self, data):
        print(self, "received data: ", data)

if __name__ == "__main__":
    print("Main is called ")
    pcServer = PCServer()
    myplayer = MyPlayer()

    print("Registering myplayer in observers for PCServer ")
    pcServer.register(myplayer)

    pcServer.serve_forever()


