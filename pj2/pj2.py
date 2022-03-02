"""
回文見つける
"""
import load_dictionary

word_list = load_dictionary.load('data/6of12.txt')
pali_list = []

for word in word_list[:5]:
    print(word)