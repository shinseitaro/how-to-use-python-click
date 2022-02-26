import asyncio
import random
import click

import pokemon

default_savedir = "./pokemons"

# command のグループ化
@click.group()
def cli():
    pass


@cli.command(help=f"ランダムに選んだポケモンを1匹ゲットします。保存先は {default_savedir} です。")
def get_a_pokemon():
    n = random.randint(1, 800)
    asyncio.run(pokemon.download_a_pokemon(n, default_savedir))


@cli.command(help="ランダムに選んだポケモンを10匹ゲットします")
def get_10_pokemons():
    asyncio.run(pokemon.download_pokemons_randomly(10, default_savedir))


@cli.command(help="指定されたID番号のポケモンをゲットします. ")
@click.option(
    "--savedir", default=default_savedir, help=f"保存先を指定。デフォルトは {default_savedir} です。"
)
@click.argument("id")
def get_pokemon(id, savedir):
    asyncio.run(pokemon.download_a_pokemon(id, savedir))


@cli.command(help="指定された数だけランダムにポケモンゲットします。")
@click.option(
    "--savedir", default=default_savedir, help=f"保存先を指定。デフォルトは {default_savedir} です。"
)
@click.argument("num")
def get_many_pokemons(num, savedir):
    asyncio.run(pokemon.download_pokemons_randomly(num, savedir))


if __name__ == "__main__":
    cli()
