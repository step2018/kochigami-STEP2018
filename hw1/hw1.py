#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

class DICTIONARY():
    def __init__(self):
        self.data = []
        self.data_dict_sorted = {}
        self.data_dict = {}
        self.read_dictionary("dictionary.txt")
        self.create_dict()
        self.sort_dict()

    def read_dictionary(self, dictionary_name):
        # 辞書の読み込み
        dict_data_tmp = open(dictionary_name, "r")
        for line in dict_data_tmp:
            self.data.append(line)
        dict_data_tmp.close()

    def create_dict(self):
        # separate by number of chars
        self.data_dict[2] = []
        self.data_dict[3] = []
        self.data_dict[4] = []
        self.data_dict[5] = []
        self.data_dict[6] = []
        self.data_dict[7] = []
        self.data_dict[8] = []
        self.data_dict[9] = []
        self.data_dict[10] = []
        self.data_dict[11] = []
        self.data_dict[12] = []
        self.data_dict[13] = []
        self.data_dict[14] = []
        self.data_dict[15] = []
        self.data_dict[16] = []
        self.data_dict[17] = []
        self.data_dict[18] = []

        for word in self.data:
            # 単語の分割．文字を一つずつ取り出す
            chars = list(word.lower())
            # ex. chars: ['b', 'l', 'a', 'd', 'e', 's', '\n'] need to delete \n
            chars[len(chars)-1:]=[]
            self.data_dict[len(chars)].append(chars)

    def sort_dict(self):
        self.data_dict_sorted[2] = []
        self.data_dict_sorted[3] = []
        self.data_dict_sorted[4] = []
        self.data_dict_sorted[5] = []
        self.data_dict_sorted[6] = []
        self.data_dict_sorted[7] = []
        self.data_dict_sorted[8] = []
        self.data_dict_sorted[9] = []
        self.data_dict_sorted[10] = []
        self.data_dict_sorted[11] = []
        self.data_dict_sorted[12] = []
        self.data_dict_sorted[13] = []
        self.data_dict_sorted[14] = []
        self.data_dict_sorted[15] = []
        self.data_dict_sorted[16] = []
        self.data_dict_sorted[17] = []
        self.data_dict_sorted[18] = []
        # ソートされた辞書の作成
        for key in self.data_dict.keys():
            for word in self.data_dict[key]:
                word_sorted = sorted(word)
                self.data_dict_sorted[len(word)].append(word_sorted)

if __name__ == '__main__':
    dictionary = DICTIONARY()
    # 文字の入力
    s = raw_input("Enter alphabets: ")
    # sのソート
    s = list(s.lower())
    s.sort()
    count = len(s)
    found = False
    # 辞書の中の文字数が多いものから検索
    for i in range(count, 1, -1):
        for word_count in range(len(dictionary.data_dict_sorted[i])):
            intersection = list(set(dictionary.data_dict_sorted[i][word_count]) & (set(s)))
            if len(intersection) == len(dictionary.data_dict_sorted[i][word_count]):
                print ("I found: {}").format(''.join(dictionary.data_dict[i][word_count]))
                found = True
                break
        if found:
            break
