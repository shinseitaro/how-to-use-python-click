import os
import random
import asyncio
import aiohttp
from logzero import logger


async def get_pokemon(session, url, png_path):
    async with session.get(url) as resp:
        html = await resp.json()
        async with session.get(html["sprites"]["front_default"]) as png:
            with open(png_path, "wb") as f:
                f.write(await png.read())
                logger.info(f"DOWNLOADING TO {png_path}")


async def download_a_pokemon(num, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    async with aiohttp.ClientSession() as session:
        logger.info(f"Getting Pokemon {num}")
        url = f"https://pokeapi.co/api/v2/pokemon/{num}"
        png_path = os.path.join(save_dir, f"{num}.png")
        await get_pokemon(session, url, png_path)


async def download_pokemons_randomly(n, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    async with aiohttp.ClientSession() as session:
        tasks = list()
        for num in random.sample(range(1, 800), n):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            png_path = os.path.join(save_dir, f"{num}.png")
            tasks.append(asyncio.create_task(get_pokemon(session, url, png_path)))

        for pokemon in asyncio.as_completed(tasks):
            await pokemon
