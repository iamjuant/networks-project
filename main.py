from src.ssh_server import SshServer

if __name__ == '__main__':
    # How to Generate your SSH keys
    #
    # Linux:
    # use the command `ssh-keygen -A` in terminal 
    # to generate all of your SSH keys. Once the command is run,
    # you can find the RSA key in the following location: ~/.ssh/id_rsa, or /home/username/.ssh/id_rsa

    #if you chose to generate ssh-keygen -A it will automatically add the RSA key in /home/username/.ssh/id_rsa
    server = SshServer('/home/kali/.ssh/id_rsa')

    # Start the server, you can give it a custom IP address and port, or
    # leave it empty to run on 127.0.0.1:22
    server.start()