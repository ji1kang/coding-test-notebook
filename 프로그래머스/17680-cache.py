# https://school.programmers.co.kr/learn/courses/30/lessons/17680#
# 캐시

def solution(cacheSize, cities):
    from collections import deque
    answer = 0
    cache = []
    
    for c in cities:
        if cacheSize == 0:
            answer += 5
            continue
        
        c = c.lower()
        
        if c in cache:
            answer += 1
            cache.remove(c)
            
        else:
            answer += 5
                
            if len(cache) >= 30 or len(cache) == cacheSize:
                cache.pop(0)
                
        cache.append(c)
            
            
    return answer
