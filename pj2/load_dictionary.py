"""
テキストファイルをリストとして読み込むモジュール.

:argument
- テキストファイル名

:exception
- ファイルが見つからなかった時の IOError

:returns
- テキストファイルにある全ての単語を小文字にしたリスト

import sysが必要
"""
import sys

def load(file):
    """テキストファイルを開いて、内容を小文字の文字列のリストに変換する"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f'{e}\nError opening [{file}]. Terminating program.', file=sys.stderr)
        sys.exit(1)