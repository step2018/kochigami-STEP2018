#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DICTIONARY():
    def __init__(self):
        self.data = []
        self.data_dict = {}
        self.read_dictionary("dictionary.txt")
        self.create_dict()

    def read_dictionary(self, dictionary_name):
        # 辞書の読み込み
        dict_data_tmp = open(dictionary_name, "r")
        for line in dict_data_tmp:
            self.data.append(line)
        dict_data_tmp.close()

    def create_dict(self):
        # separate by number of chars of a word
        # ex. "rabbit" enters data_dict[6]
        # You might want to initialize this using list comprehension for simplicity:
        self.data_dict = {len: [] for len in range(2,19)}

        for word in self.data:
            # 単語の分割．文字を一つずつ取り出してリストに入れる
            chars = list(word.lower().rstrip()) # rstripで空白を簡単に消せる（これでもし空白じゃなかったら間違って意味のある文字は消されない）
            # ex. chars: ['b', 'l', 'a', 'd', 'e', 's']
            self.data_dict[len(chars)].append(chars)

'''
入力文字列 s_p に 辞書の単語 tag_p の各文字が含まれているかを調べる関数
'''
def find_common_char(tag_p, s_p):
    tag_p_cp = tag_p[:]
    s_p_cp = s_p[:]
    found_list = []
    count = 0
    # len(tag_p_cp) =< len(s_cp_p) がこのプログラムでは常に成り立つので，tag_cp_pが先に空になる
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

'''
s: 入力文字列　（ゲームで与えられる文字の列）
count: sの長さ
dictionary.data_dict: 辞書の単語をアルファベット順ではなく，文字の長さで分けたもの（辞書）
dictionary.data_dict[i][word_count]: iは文字の長さ(2-18にした)，word_countはそのうち何番目か
                                     ex. dictionary.data_dict[12][0] => ['a', 'f', 'r', 'o', 'c', 'e', 'n', 't', 'r', 'i', 's', 'm']
intersection: s とdictionary.data_dict[i][word_count] で被っている文字のリスト
              ex. s: ['m', 'o', 'o', 'n'] と dictionary.data_dict[i][word_count]: ['m', 'o', 'o', 'o', 'm'] なら，['m', 'o', 'o']
candidate:     sを元に出来た単語の文字列リスト（最高点計算用）
               ex. [['m', 'o', 'o', 'n'], [...], [...]]
candidate_tag: sを元に出来た単語の文字列リスト（最終結果表示用）
               ex. ['moon', '...', '...']
point: candidateそれぞれの得点（正確な計算ではないが十分な計算）
max_idx: 最高点を出すcandidateのインデックス
'''

if __name__ == '__main__':
    dictionary = DICTIONARY()
    # 終了はCtrl+cで行う
    while True:
        # 文字の入力
        s = raw_input("Enter alphabets: ")
        # sのアルファベットを全て小文字にして，リストに一つずつ入れる
        s = list(s.lower())
        count = len(s)
        candidate = []
        candidate_tag = []
        # 辞書の中の文字数が多いものから検索
        for i in range(count, 1, -1):
            for word_count in range(len(dictionary.data_dict[i])):
                # 辞書の単語の文字が 入力文字列に含まれているか調べる
                # 含まれている文字をリストに入れていく
                intersection = find_common_char(dictionary.data_dict[i][word_count], s)
                # もし上で出来たリストと辞書の単語のリストの長さが一緒なら，文字が全部含まれていることになる
                if len(intersection) > 0 and len(intersection) == len(dictionary.data_dict[i][word_count]):
                    # candidate: 最高点計算用の文字列リスト
                    # ex. [['m', 'o', 'o', 'n'], [...], [...]]
                    candidate.append(intersection)
                    # candidate_tag: 最終結果表示用の文字列リスト
                    # ex. ['moon', '...', '...']
                    candidate_tag.append(''.join(dictionary.data_dict[i][word_count]))

        # candidateから点数の高いものを選ぶ
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

        if len(point) > 0:
            max_idx = point.index(max(point))
            print ("I found: {} {}").format(candidate_tag[max_idx], max(point))
        else:
            print "PASS"
