import asyncio
import random
from colorama import Fore, Style

CLIENTS = {}


async def generate_random_color():
    return random.choice(
        [
            Fore.RED,
            Fore.GREEN,
            Fore.YELLOW,
            Fore.BLUE,
            Fore.MAGENTA,
            Fore.CYAN,
            Fore.WHITE,
        ]
    )


async def broadcast_message(message, exclude_writer=None):
    for client in CLIENTS.values():
        if client["w"] is not exclude_writer:
            try:
                client["w"].write(message.encode())
                await client["w"].drain()
            except ConnectionError:
                pass


async def handle_client(reader, writer):
    addr = writer.get_extra_info("peername")
    first_data = await reader.read(1024)
    pseudo = (
        first_data.decode().split("|")[1].strip()
        if first_data.startswith(b"Hello|")
        else "Inconnu"
    )

    color = await generate_random_color()

    CLIENTS[addr] = {"r": reader, "w": writer, "pseudo": pseudo, "color": color}
    await broadcast_message(
        f"{color}{pseudo} se joint à la discussion{Style.RESET_ALL}"
    )

    while True:
        data = await reader.read(1024)
        if not data:
            message = f"{color}{pseudo} s'en va{Style.RESET_ALL}"
            del CLIENTS[addr]
            await broadcast_message(message, exclude_writer=writer)
            break
        message = f"{color}{pseudo} réplique : {data.decode()}{Style.RESET_ALL}"
        await broadcast_message(message, exclude_writer=writer)

    writer.close()


async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8888)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
