import sys
import socket
import thread


# serve the client by echoing each message with my name
def serve_client(clientSock):

    while True:
        data = clientSock.recv(1024)
        reply = data + " Konrad"

        if not data:
            break

        clientSock.sendall(reply)

    clientSock.close()

def main():

    try:
        try:
            # open socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', 8888))
            sock.listen(5)
        except socket.error as msg:
            print "Failed to created server socket"
            print "Error code: " + str(msg[0]) + " - " + msg[1]
            sys.exit()

        while True:
            try:
                # serve each client in a thread
                (clientSock, address) = sock.accept()
                thread.start_new_thread(serve_client, (clientSock,))
            except socket.error as msg:
                print "Failed to created client socket"
                print "Error code: " + str(msg[0]) + " - " + msg[1]
    finally:
        sock.close()

if __name__ == "__main__":
    main()
