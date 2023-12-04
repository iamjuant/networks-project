from abc import ABC, abstractmethod
from sys import platform
import socket, threading
import sqlite3
class ServerBase(ABC):

    def __init__(self):
        # create a multithreaded event, which is basically a
        # thread-safe boolean
        self._is_running = threading.Event()

        # this socket will be used to listen to incoming connections
        self._socket = None

        # this will contain the shell for the connected client.
        # we don't yet initialize it, since we need to get the
        # stdin and stdout objects after the connection is made.
        self.client_shell = None

        # this will contain the thread that will listen for incoming
        # connections and data.
        self._listen_thread = None

    # To start the server, we open the socket and create 
    # the listening thread.
    def start(self, address='127.0.0.1', port=22, timeout=1):
        if not self._is_running.is_set():
            self._is_running.set()

            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

            # reuse port is not avaible on windows
            if platform == "linux" or platform == "linux2":
                self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)

            self._socket.settimeout(timeout)
            self._socket.bind((address, port))

            self._listen_thread = threading.Thread(target=self._listen)
            self._listen_thread.start()

    # To stop the server, we must join the listen thread
    # and close the socket.
    def stop(self):
        if self._is_running.is_set():
            self._is_running.clear()
            self._listen_thread.join()
            self._socket.close()

    def checkIPfromDB(self,client):
        conn = sqlite3.connect("UserCredentials.db")
        cursor = conn.cursor()
        print("check ip from db")
        print("192.168.30.11")
        cursor.execute('SELECT * FROM whitelist WHERE ip = ?',("192.168.30.11",))
        # cursor.execute('SELECT * FROM whitelist WHERE ip = ?',(client[0],))
#         cursor.execute('select * from whitelist where ip = ?',(session.getpeername()[0]))
        conn.commit()
        rows = cursor.fetchall()
        conn.close()
        if(rows):
            print(rows)
        else:
            print("The IP",client[0],"is not allowed")
        return rows
    # The listen function will constantly run if the server is running.
    # We wait for a connection, if a connection is made, we will call 
    # our connection function.
    def _listen(self):
        while self._is_running.is_set():
            try:
                self._socket.listen()
                client, addr = self._socket.accept()
                print(addr)
                result = self.checkIPfromDB(addr)
                if(result):
                    self.connection_function(client)
                self.stop()
            except socket.timeout:
                pass

     
    @abstractmethod
    def connection_function(self, client):
        pass