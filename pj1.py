"""
名前生成ジェネレーター：
2つのタプルからランダムに名前を選んで画面に表示する。
"""
import random
import sys

def main():
    """２つのタプルからランダムに名前を選んで画面に表示する"""

    first = ("hoge", "fuga", "piyo")
    last = ("abc", "def", "ghi")

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print(f'{first_name} {last_name}', file=sys.stderr)

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
