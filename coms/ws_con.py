"""
ws_con.py

This module provides a class-based, configurable WebSocket client for connecting to WebSocket servers.

Classes:
    WebSocketClient: A configurable WebSocket client supporting connect, send, receive, and close operations.
"""

import asyncio
import websockets


class WebSocketClient:
    """
    A configurable, OOP-compatible WebSocket client.

    Args:
        host (str): The WebSocket server host. Defaults to "localhost".
        port (int): The WebSocket server port. Defaults to 8765.

    Methods:
        connect(): Connects to the WebSocket server.
        send(message): Sends a message to the server.
        receive(): Receives a message from the server.
        close(): Closes the connection.
        run(message): Example method to demonstrate usage.
    """

    def __init__(self, host="localhost", port=8765):
        """
        Initialize the WebSocketClient.

        Args:
            host (str): The WebSocket server host.
            port (int): The WebSocket server port.
        """
        self.host = host
        self.port = port
        self.uri = f"ws://{self.host}:{self.port}"
        self.websocket = None

    async def connect(self):
        """Establish the WebSocket connection."""
        self.websocket = await websockets.connect(self.uri)
        print(f"Connected to {self.uri}")

    async def send(self, message):
        """Send a message to the WebSocket server."""
        if self.websocket:
            await self.websocket.send(message)
            print(f"Sent: {message}")

    async def receive(self):
        """Receive a message from the WebSocket server."""
        if self.websocket:
            response = await self.websocket.recv()
            print(f"Received: {response}")
            return response

    async def close(self):
        """Close the WebSocket connection."""
        if self.websocket:
            await self.websocket.close()
            print("Connection closed.")

    async def run(self, message="Hello, WebSocket!"):
        """Example run method for demonstration."""
        await self.connect()
        await self.send(message)
        await self.receive()
        await self.close()


if __name__ == "__main__":
    import sys

    host = input("Enter WebSocket host (default: localhost): ") or "localhost"
    port_input = input("Enter WebSocket port (default: 8765): ")
    port = int(port_input) if port_input else 8765

    client = WebSocketClient(host, port)
    asyncio.run(client.run())
