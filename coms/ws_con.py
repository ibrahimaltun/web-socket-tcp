import asyncio
import websockets

async def connect_to_websocket(uri):
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {uri}")
        # Example: send a message
        await websocket.send("Hello, WebSocket!")
        # Example: receive a message
        response = await websocket.recv()
        print(f"Received: {response}")

if __name__ == "__main__":
    uri = "ws://localhost:8765"  # Change to your WebSocket server URI
    asyncio.run(connect_to_websocket(uri))