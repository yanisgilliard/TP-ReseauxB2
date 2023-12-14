import aiohttp
import aiofiles
import asyncio
import sys

async def get_content(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"Une erreur s'est produite lors de la récupération du contenu : {e}")
        return None

async def write_content(content, file_path):
    try:
        async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
            await file.write(content)
        print(f"Le contenu a été écrit dans le fichier : {file_path}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'écriture du contenu dans le fichier : {e}")

async def main(url):
    content = await get_content(url)

    if content:
        file_path = '/tmp/web_page'
        await write_content(content, file_path)
    else:
        print("Impossible de récupérer le contenu de la page.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    asyncio.run(main(url))