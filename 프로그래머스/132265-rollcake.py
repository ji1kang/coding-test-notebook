# https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 롤케이크 자르기 

def solution(topping):
    from collections import Counter
    answer = 0
    n = len(topping)
    
    u1 = {}
    u2 = dict(Counter(topping))
    

    for i in topping:
        val = u1.get(i, 0)
        if val == 0:
            u1[i] = 1
        else:
            u1[i] = val + 1
        
        val = u2.get(i)
        if val == 1:
            del u2[i]
        else:
            u2[i] = val - 1
            
        if len(u1) == len(u2):
            answer += 1
        
    
    return answer
