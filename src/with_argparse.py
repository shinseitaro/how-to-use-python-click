import argparse
import random
import pokemon

# てきとうに一匹、デフォルトの場所に
# てきとうに一匹、指定の場所に
# 指定の一匹、デフォルトの場所に
# 指定の一匹、指定の場所に
# 同上をてきとうな、ｎ匹にも


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--random", help="ポケモンを適当に一匹ゲットします", action="store_true")
    args = parser.parse_args()

    if args.random:
        n = random.randint(1, 800)
        pokemon.download_a_pokemon(n, save_dir)


if __name__ == "__main__":
    main()
