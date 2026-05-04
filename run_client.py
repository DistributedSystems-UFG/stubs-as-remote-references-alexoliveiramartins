from client import Client
from constRPC import *
from dbclient import DBClient

def run():
    c = Client(PORT_CLIENT)
    db = DBClient(SERVER_ADDR, PORT)

    db.create()
    db.appendData("Client N")
    print(db.getValue())

    input("Digite qualquer coisa para parar o servidor (STOP): ")
    db.stop()

if __name__ == '__main__':
    run()