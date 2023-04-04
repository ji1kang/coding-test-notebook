# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    # 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.
    
    from collections import Counter
    
    freq = Counter(tangerine).most_common()
    
    
    kind = 0
    cumsum = 0
    
    
    for key, val in freq:
        if  cumsum < k:
            cumsum += val
            kind += 1
        
            
    
    return kind #  k개를 고를 때 서로 다른 종류의 수의 최솟값
