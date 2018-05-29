#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

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
    found = False
    for i in range(len(s), 1, -1):
        p = itertools.combinations(s, i)
        for j in p:
            for word_count in range(len(dictionary.data_sorted)):
                # 辞書と入力文字を比較
                # 総当り戦
                if list(j) == dictionary.data_sorted[word_count]:
                    print ("I found: {}").format(dictionary.data[word_count])
                    found = True
                    break
            if found:
                break
        if found:
            break
    '''
    I could not treat multiple same char
    ex.
    ('m', 'n', 'o') (print j)
    I found: Mon

    ('m', 'n', 'o')
    I found: Mon
    '''
    '''
    kochigami@kochigami-ThinkPad-T450:~/STEP2018/hw1$ python hw1.py 
    Enter alphabets: moon
    ('m', 'n', 'o', 'o')
    I found: Moon

    ('m', 'n', 'o')
    I found: Mon

    ('m', 'n', 'o')
    I found: Mon

    ('m', 'o', 'o')
    I found: moo

    ('n', 'o', 'o')
    I found: Ono

    ('m', 'n')
    ('m', 'o')
    ('m', 'o')
    ('n', 'o')
    ('n', 'o')
    ('o', 'o')
    '''
        
