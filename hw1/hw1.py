#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DICTIONARY():
    def __init__(self):
        self.data = []
        self.data_sorted = []
        self.read_dictionary("dictionary.txt")

    def read_dictionary(self, dictionary_name):
        # 辞書の読み込み
        dict_data_tmp = open(dictionary_name, "r")
        for line in dict_data_tmp:
            self.data.append(line)
        dict_data_tmp.close()

        # ソートされた辞書の作成
        for word in self.data:
            # 単語の分割．文字を一つずつ取り出す
            chars = list(word.lower())
            # ex. chars: ['b', 'l', 'a', 'd', 'e', 's', '\n'] need to delete \n
            chars[len(chars)-1:]=[]
            chars.sort()
            self.data_sorted.append(chars)

if __name__ == '__main__':
    dictionary = DICTIONARY()
    # 文字の入力
    s = raw_input("Enter alphabets: ")
    # sのソート
    s = list(s.lower())
    s.sort()

    # 辞書と入力文字を比較
    for word_count in range(len(dictionary.data_sorted)):
        if s == dictionary.data_sorted[word_count]:
            print ("I found: {}").format(dictionary.data[word_count])
            break

    '''
    kochigami@kochigami-ThinkPad-T450:~/STEP2018/hw1$ python hw1.py 
    Enter alphabets: moonstarer
    I found: astronomer
    '''
        
