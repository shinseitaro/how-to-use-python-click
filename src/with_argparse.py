import argparse
import asyncio
import random
import pokemon


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r", "--random", help="ランダムに選んだポケモンを1匹ゲットします", action="store_true"
    )
    parser.add_argument(
        "-i",
        "--id",
        help="ポケモンIDを指定",
    )
    parser.add_argument(
        "-d",
        "--savedir",
        help="保存先を指定",
    )
    parser.add_argument("--get10", help="ランダムに選んだポケモンを10匹ゲットします", action="store_true")
    parser.add_argument("--getmany", help="指定された数だけランダムにポケモンゲットします。-d で保存先を指定可")

    args = parser.parse_args()
    default_savedir = "./pokemons"

    if args.random:
        n = random.randint(1, 800)
        asyncio.run(pokemon.download_a_pokemon(n, default_savedir))

    if args.get10:
        asyncio.run(pokemon.download_pokemons_randomly(10, default_savedir))

    if args.id and args.savedir:
        n = args.id
        save_dir = args.savedir
        asyncio.run(pokemon.download_a_pokemon(n, save_dir))

    if args.getmany:
        num = int(args.getmany)
        if args.savedir:
            save_dir = args.savedir
        else:
            save_dir = args.default_savedir
        asyncio.run(pokemon.download_pokemons_randomly(num, save_dir))


if __name__ == "__main__":
    main()
