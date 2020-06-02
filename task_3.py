import socket
import threading

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    try:
        c = s.connect((ip, port))
        print(port + ' is open')
        c.close()
    except:
        pass


if __name__ == "__main__":
    ip = 'localhost'
    for i in range(1000):
        thread = threading.Thread(target=scan_port, args=(ip, i))
        thread.start()
        thread.join()
