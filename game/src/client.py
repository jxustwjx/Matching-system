from match_client.match import Match
from match_client.match.ttypes import User

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from sys import stdin #python3标准读入

def operate(op, user_id, username, score):
    # Make socket
    transport = TSocket.TSocket('127.0.0.1', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Match.Client(protocol)

    # Connect!
    transport.open()

    user = User(user_id, username, score)

    if op == "add":
        client.add_user(user, "")
    elif op == "remove":
        client.remove_user(user, "")

    # Close!
    transport.close()

def main():
    for line in stdin:      #从终端读入数据，以空格隔开数据
        op, user_id, username, score = line.split(' ')
        operate(op, int(user_id), username, int(score))


if __name__ == "__main__":
    main()

