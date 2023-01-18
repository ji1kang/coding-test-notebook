# https://school.programmers.co.kr/learn/courses/30/lessons/17677#
def solution(str1, str2):
    import re
    
    if len(str1) == 0 or len(str2)==0:
        return 65536
        
    
    def pre(s):
        sublist = []
        for i in range(len(s)-1):
            if s[i].isalpha() and s[i+1].isalpha():
                item = s[i] + s[i+1]
                sublist.append(item.lower())
            
        return sublist

    str1 = pre(str1)
    str2 = pre(str2)
    
    print(str1, str2)
    inter = 0

    for s in str1:
        if s in str2:
            inter += 1
            str2.remove(s)
    
    uni = len(str1) + len(str2) 
    
    if uni == 0:
        return 65536
    elif inter == 0:
        return 0
    else:
        answer = (inter / uni) * 65536
        return int(answer)
    
