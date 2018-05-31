#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
入力文字列 s_p に 辞書の単語 tag_p の各文字が含まれているかを調べる関数
重複する文字もきちんとカウントしたいので，この関数を作った

ex. 
tag_p=['2','7','1','1','4','6']
s_p=['7','1','1','2','7','7','4','8','9']

=> ['2', '7', '1', '1', '4']
'''

tag_p=[2,7,1,1,4,6]
s_p=[7,1,1,2,7,7,4,8,9]

tag_p=['2','7','1','1','4','6']
s_p=['7','1','1','2','7','7','4','8','9']

def find_common_char(tag_p, s_p):
    found_list = []
    count = 0
    # len(tag_p) < len(s_p) という前提
    # tag_pが先に空になる
    while tag_p!=[]:
        count = 0
        for s in range(len(s_p)):
            count +=1
            if tag_p[0] == s_p[s]:
                found_list.append(tag_p[0])
                del tag_p[0]
                del s_p[s]
                break
            if count == len(s_p):
                del tag_p[0]
                break

    return found_list
            
print find_common_char(tag_p, s_p)
