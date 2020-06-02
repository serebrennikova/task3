import socket
from contextlib import closing
import threading


def parser_file(file):
    global start, end
    with open(file) as f:
        content = f.read()
    content = content.split("\n")
    start = int(content[0])
    end = int(content[1])


def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    try:
        with closing(s.connect((ip, port))):
            print(port)
    except:
        pass


if __name__ == "__main__":
    start = 0
    end = 0
    parser_file("range.txt")
    ip = "localhost"
    for i in range(start, end):
        thread = threading.Thread(target=check_port, args=(ip, i))
        thread.start()
        thread.join()
