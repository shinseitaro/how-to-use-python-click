# Click の 使い方

[PyLadies Tokyo Meetup #67 推しライブラリショートセッション](https://pyladies-tokyo.connpass.com/event/236789/)の LT 資料


## 公式Doc
[Welcome to Click — Click Documentation (8.0.x)](https://click.palletsprojects.com/en/8.0.x/)


## Click とは
- `Command Line Interface Creation Kit` 
- コマンドラインインターフェイス
- Flask つくった [The Pallets Projects](https://palletsprojects.com/) というところが作っているみたいですよ。


## 何に困っていた？

- 従来のCLIライブラリといえば、argparse 
    - （以下全部、個人の意見です）
        - まー分かりづらい。
        - まどろっこしい。
        - なげーよ。覚えれないわ。
        - 実際実行する関数、遠いわ。
        - 実行時に渡す引数名のセンスが問われて嫌なんだよ。（わかりにくいだの、長過ぎるだの、うっせー）


###  簡単な `argparse` の説明
```python
# run.py
import argparse

def hello(f):
    if f:
        print("Hello Pyladies トーキョー!")

def main():
    # 1. ArgumentParser オブジェクト作成
    parser = argparse.ArgumentParser() 

    # 2. add_argument() メソッドで引数を追加する
    parser.parse_args("-f", "--flag", action="action_store", help="Pyladiesにあいさつします")

    # 3. parse_args()　メソッドで引数を解析する
    args = parser.parse_args()

    # 4. とある引数があれば、対応する処理を行う。
    if args.flag:
        hello(args.flag)

if __name__ == "__main__":
    main()
```
```bash
python run.py -f
```




## 今回の押し `Click` 

- `@click.command()` デコレータで実行したい関数を包むという特殊性以外は直感的！
- 実際に実行する関数が近くにあってわかりやすい
- 呼び出し時に関数名を引数に渡せる！


```python
# run.py
import click

# command のグループ化
# 「コマンドラインのグループ名を作成」というイメージでOK
@click.group()
def cli():
    pass


# コマンドラインで使いたい関数を @cli.command() デコレータで包む
@cli.command(help="Pyladiesにあいさつします")
@click.option("-f", "--flag", default=True)
def hello(flag):
    if flag:
        print("Hello Pyladies トーキョー!")


if __name__ == "__main__":
    cli()
```
```bash
python run.py hello
```

[これですよこれ。こういうのでいいんですよ。](https://dic.nicovideo.jp/a/%E3%81%93%E3%81%86%E3%81%84%E3%81%86%E3%81%AE%E3%81%A7%E3%81%84%E3%81%84%E3%82%93%E3%81%A0%E3%82%88%E3%81%93%E3%81%86%E3%81%84%E3%81%86%E3%81%AE%E3%81%A7)


 <img src="https://livedoor.blogimg.jp/pom2-pom2/imgs/4/5/45470528.jpg" width="30%">    


## LT用スクリプト

- [PokéAPI](https://pokeapi.co/docs/v2#fairuse)を使ってポケモンをゲットするスクリプト
- コマンドラインから以下のオプションを渡せます
    1. ランダムにポケモンを1匹ダウンロード
    1. 指定のポケモンを1匹ダウンロード
    1. ポケモンをｎ匹ランダムにダウンロード
    1. 保存先はオプションで指定可

### argparse で書いた場合 
[src/with_argparse.py](src/with_argparse.py)

### click で書いた場合 
[src/with_click.py](src/with_click.py)
   


## 参照：
- [Argparse チュートリアル — Python 3.9.4 ドキュメント](https://docs.python.org/ja/3.9/howto/argparse.html)
- [Welcome to Click — Click Documentation (8.0.x)](https://click.palletsprojects.com/en/8.0.x/)
- [AIOHTTP Client デモ — AIOHTTPハンズオン ドキュメント](https://aiohttp-hands-on.readthedocs.io/ja/latest/aiohttp_client_demo.html)










