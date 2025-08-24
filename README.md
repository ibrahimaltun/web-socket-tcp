# WebSocket and TCP Communication Module

This project provides simple, class-based, and configurable Python modules for both TCP and WebSocket communication. You can use these modules to quickly set up TCP or WebSocket clients and servers for your networking projects.

---

## Features

- **TCP Communication**
  - Class-based TCP server and client
  - Easy to configure host and port
  - Simple send/receive message interface

- **WebSocket Communication**
  - Class-based WebSocket client
  - Configurable host and port
  - Asynchronous send/receive interface using `asyncio`

---

## Requirements

- Python 3.7+
- For WebSocket: `websockets` library  
  Install with:
  ```sh
  pip install websockets
  ```

---

## Usage

### TCP Communication

#### TCP Server

Run the TCP server:
```sh
python coms/tcp_coms.py server
```
- Listens on `127.0.0.1:9000` by default.
- Receives a message from a client and sends a response.

#### TCP Client

Run the TCP client:
```sh
python coms/tcp_coms.py
```
- Connects to `127.0.0.1:9000` by default.
- Sends a message to the server and prints the response.

You can modify the host and port in the code or extend the classes for your needs.

---

### WebSocket Communication

#### WebSocket Client

Run the WebSocket client:
```sh
python coms/ws_con.py
```
- You will be prompted to enter the WebSocket server host and port (defaults: `localhost:8765`).
- Connects to the server, sends a message, receives a response, and closes the connection.

---

## Code Structure

- `coms/tcp_coms.py`  
  Contains `TCPServer` and `TCPClient` classes with docstrings and example usage.

- `coms/ws_con.py`  
  Contains `WebSocketClient` class with docstrings and example usage.

---

## Example

**TCP Example:**
1. Start the server:
   ```sh
   python coms/tcp_coms.py server
   ```
2. In another terminal, start the client:
   ```sh
   python coms/tcp_coms.py
   ```

**WebSocket Example:**
1. Make sure you have a WebSocket server running (for example, using [websocat](https://github.com/vi/websocat) or your own server).
2. Run the client:
   ```sh
   python coms/ws_con.py
   ```

---

## Customization

- Change host and port by editing the class initialization or passing parameters.
- Extend the classes to add authentication, persistent connections, or custom message handling.

---

## License

MIT License

---

## Author
@ibrahimaltun