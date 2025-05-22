import time
import socket

def wait_for_port(port, host="localhost", timeout=5.0):
    start = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return
        except OSError:
            if time.time() - start > timeout:
                raise RuntimeError(f"Timeout waiting for port {port}")
            time.sleep(0.1)
