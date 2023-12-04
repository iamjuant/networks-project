import paramiko
import sqlite3
from src.server_base import ServerBase
from src.ssh_server_interface import SshServerInterface
from src.shell import Shell

class SshServer(ServerBase):

    def __init__(self, host_key_file, host_key_file_password=None):
        super(SshServer, self).__init__()

        self._host_key = paramiko.RSAKey.from_private_key_file(host_key_file, host_key_file_password)

    def connection_function(self, client):
        try:
            
            # print(client.getpeername()[0])
            # create the SSH transport object
            
            session = paramiko.Transport(client)
            
            session.add_server_key(self._host_key)

            
            # create the server
            server = SshServerInterface()

            # start the SSH server
            try:
        #         conn = sqlite3.connect("UserCredentials.db")
        #         cursor = conn.cursor()
        #         cursor.execute(
        #   'select * from credentials where username = ?',('iamjuant'))
        # #         cursor.execute('select * from whitelist where ip = ?',(session.getpeername()[0]))
        #         conn.commit()
        #         rows = cursor.fetchall()
        #         conn.close()
        #         print(rows)
                session.start_server(server=server)
                # if (rows):
                #     print(session.getpeername()[0])
                # else:
                #     print("your IP address is not allowed")
                #     session.close()
            except paramiko.SSHException:
                return

            # create the channel and get the stdio
            channel = session.accept()
            print(channel.getpeername()[0])
            print(channel.getpeername()[1])
            stdio = channel.makefile('rwU')

            # create the client shell and start it
            # cmdloop() will block execution of this thread.
            self.client_shell = Shell(stdio, stdio)
            self.client_shell.cmdloop()

            # After execution continues, we can close the session
            # since the only way execution will continue from
            # cmdloop() is if we explicitly return True from it,
            # which we do with the bye command.
            session.close()
        except:
            pass