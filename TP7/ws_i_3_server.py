import asyncio
import websockets

CLIENTS = {}


async def broadcast_message(message, exclude=None):
    for client in CLIENTS.values():
        if client is not exclude:
            try:
                await client.send(message)
            except websockets.exceptions.ConnectionClosed:
                pass


async def handle_client(websocket):
    addr = websocket.remote_address
    first_data = await websocket.recv()
    pseudo = (
        first_data.split("|")[1].strip()
        if first_data.startswith("Hello|")
        else "Inconnu"
    )
    CLIENTS[addr] = websocket
    await broadcast_message(f"Annonce : {pseudo} a rejoint la chatroom")

    try:
        async for message in websocket:
            broadcast_msg = f"{pseudo} a dit : {message}"
            await broadcast_message(broadcast_msg, exclude=websocket)
    except websockets.exceptions.ConnectionClosed:
        pass

    del CLIENTS[addr]
    await broadcast_message(f"Annonce : {pseudo} a quitté la chatroom")


async def main():
    async with websockets.serve(handle_client, "127.0.0.1", 8888):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
