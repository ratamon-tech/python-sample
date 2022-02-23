import random
import sys

first = ("hoge", "fuga", "piyo")
last = ("abc", "def", "ghi")

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print(f'{firstName} {lastName}', file=sys.stderr)

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")