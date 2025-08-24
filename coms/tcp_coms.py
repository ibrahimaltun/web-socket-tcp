"""
tcp_coms.py

This module provides TCP server and client classes for simple socket communication.

Classes:
    TCPServer: A simple TCP server that listens for a single connection, receives a message, and sends a response.
    TCPClient: A simple TCP client that connects to a server, sends a message, and receives a response.
"""

import socket


class TCPServer:
    """
    A simple TCP server.

    Args:
        host (str): The IP address to bind the server to. Defaults to "127.0.0.1".
        port (int): The port to bind the server to. Defaults to 9000.

    Methods:
        start(): Starts the server, accepts one connection, receives data, and sends a response.
    """

    def __init__(self, host="127.0.0.1", port=9000):
        """
        Initialize the TCPServer.

        Args:
            host (str): The IP address to bind the server to.
            port (int): The port to bind the server to.
        """
        self.host = host
        self.port = port

    def start(self):
        """
        Start the TCP server, accept a single connection, receive data, and send a response.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                print(f"Received: {data.decode()}")
                conn.sendall(b"Hello, TCP Client!")


class TCPClient:
    """
    A simple TCP client.

    Args:
        host (str): The server IP address to connect to. Defaults to "127.0.0.1".
        port (int): The server port to connect to. Defaults to 9000.

    Methods:
        connect(): Connects to the server, sends a message, and receives a response.
    """

    def __init__(self, host="127.0.0.1", port=9000):
        """
        Initialize the TCPClient.

        Args:
            host (str): The server IP address to connect to.
            port (int): The server port to connect to.
        """
        self.host = host
        self.port = port

    def connect(self):
        """
        Connect to the TCP server, send a message, and receive a response.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                print(f"Connected to {self.host}:{self.port}")
                s.sendall(b"Hello, TCP Server!")
                data = s.recv(1024)
                print(f"Received: {data.decode()}")
        except Exception as e:
            print(f"Connection failed: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "server":
        server = TCPServer()
        server.start()
    else:
        client = TCPClient()
        client.connect()
