import socket
import subprocess
from conftest import wait_for_port

def test_server_accepts_connection():
    proc = subprocess.Popen(["python", "main.py"])
    wait_for_port(12345)

    try:
        s = socket.socket()
        s.connect(('localhost', 12345))
        s.close()
    finally:
        proc.terminate()
