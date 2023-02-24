# https://school.programmers.co.kr/learn/courses/30/lessons/12922
# 수박수박수박수박수박수? 

def solution(n):
    from itertools import cycle
    arr = cycle('수박')
    answer = [next(arr) for _ in range(n)]
    
    return ''.join(answer)
