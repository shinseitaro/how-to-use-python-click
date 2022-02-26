import asyncio
import random
import click

import pokemon

default_savedir = "./pokemons"

# command のグループ化
@click.group()
def cli():
    pass


@cli.command(help=f"ランダムに選んだポケモンを1匹ゲットします。")
@click.option("--id", default=random.randint(1, 800), help="ID で指定したポケモンを取得します")
@click.option(
    "--savedir", default=default_savedir, help=f"保存先を指定。デフォルトは {default_savedir} です。"
)
def get_a_pokemon(id, savedir):
    asyncio.run(pokemon.download_a_pokemon(id, savedir))


@cli.command(help="ランダムに選んだポケモンを指定数匹ゲットします。デフォルトは10匹です。")
@click.option("--num", default=10, help="ゲットするポケモンの数を指定。指定しなければ10匹ゲットします")
@click.option(
    "--savedir", default=default_savedir, help=f"保存先を指定。デフォルトは {default_savedir} です。"
)
def get_pokemons(num, savedir):
    asyncio.run(pokemon.download_pokemons_randomly(num, savedir))


if __name__ == "__main__":
    cli()
