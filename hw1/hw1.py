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

def find_common_char(tag_p, s_p):
    tag_p_cp = tag_p[:]
    s_p_cp = s_p[:]
    found_list = []
    count = 0
    while tag_p_cp!=[]:
        count = 0
        for s in range(len(s_p_cp)):
            count +=1
            if tag_p_cp[0] == s_p_cp[s]:
                found_list.append(tag_p_cp[0])
                del tag_p_cp[0]
                del s_p_cp[s]
                break
            if count == len(s_p_cp):
                del tag_p_cp[0]
                break
    return found_list

if __name__ == '__main__':
    dictionary = DICTIONARY()
    while True:
        # 文字の入力
        s = raw_input("Enter alphabets: ")
        # sのソート
        s = list(s.lower())
        s.sort()
        count = len(s)
        candidate = []
        candidate_tag = []
        # 辞書の中の文字数が多いものから検索
        for i in range(count, 1, -1):
            for word_count in range(len(dictionary.data_dict_sorted[i])):
                intersection = find_common_char(dictionary.data_dict_sorted[i][word_count], s)
                if len(intersection) > 0 and len(intersection) == len(dictionary.data_dict_sorted[i][word_count]):
                    candidate.append(intersection)
                    candidate_tag.append(''.join(dictionary.data_dict[i][word_count]))

        # 点数の高いものを選ぶ
        point = []
        for word in candidate:
            tmp = 0
            for s in word:
                if s == 'j' or s == 'k' or s == 'q' or s == 'x' or s == 'z':
                    tmp+=3
                elif s == 'c' or s == 'f' or s == 'h' or s == 'l' or s == 'm' or s == 'p' or s == 'v' or s == 'w' or s == 'y':
                    tmp+=2
                else:
                    tmp+=1
            point.append(tmp)

        max_idx = point.index(max(point))
        print ("I found: {} {}").format(candidate_tag[max_idx], max(point))
