# 다음 큰 숫자 
# https://school.programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    answer = n+1
    
    while True:
        
        if bin(n).count('1') == bin(answer).count('1'):
            break
        else:
            answer += 1
            
    return answer
