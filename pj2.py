"""
回文見つける
"""
import sys

def load(file):
    """テキストファイルを開いて、内容を小文字の文字列のリストに変換する"""
    try:
        with open(file) as in_file:
            print("ok")
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("error")
        sys.exit(1)

load('6of12.txt')