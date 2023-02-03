# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 숫자의 표현 

def solution(n):
    answer = 1
    
    for i in range(n):
        cumsum = 0
        for j in range(i+1, n):
            cumsum += j
            if cumsum == n:
                answer += 1
                break
            elif cumsum > n:
                break
            
    return answer
