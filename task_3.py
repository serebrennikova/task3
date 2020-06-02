import socket
from contextlib import closing
import threading


def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    try:
        with closing(s.connect((ip, port))):
            print(port)
    except:
        pass


if __name__ == "__main__":
    ip = "localhost"
    for i in range(1000):
        thread = threading.Thread(target=check_port, args=(ip, i))
        thread.start()
        thread.join()
