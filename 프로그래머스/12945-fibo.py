# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수 
# 파이썬은 재귀가 느릴 수도 있다

def solution(n):
    data = [None] * (n+1)
    data[0] = 0
    data[1] = 1
    
    
    
    
    for i in range(2, n+1):
        data[i] = data[i-1] + data[i-2]
        
    
    answer = data[n] % 1234567
     
    return answer
