#len(tag_p) < len(s_p)

tag_p=[2,7,1,1,4,6]
s_p=[7,1,1,2,7,7,4,8,9]

tag_p=['2','7','1','1','4','6']
s_p=['7','1','1','2','7','7','4','8','9']

tag_p = ['a', 'c', 'e', 'l']
s_p = ['m', 'o', 'o', 'n']

def find_common_char(tag_p, s_p):
    found_list = []
    count = 0
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
