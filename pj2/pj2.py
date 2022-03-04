"""
辞書ファイルにある回文を見つける
"""
import load_dictionary
import os

dictionary_path = os.path.abspath('data/6of12.txt')
word_list = load_dictionary.load(dictionary_path)
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print(f'\nNumber of palindromes found = {len(pali_list)}\n')
print(*pali_list[:5], sep='\n')
print(dictionary_path)

