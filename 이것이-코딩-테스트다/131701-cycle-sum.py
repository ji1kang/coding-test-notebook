# https://school.programmers.co.kr/learn/courses/30/lessons/131701
# 연속 부분 수열 합의 개수 

def solution(elements):
    n = len(elements)
    
    answer = [sum(elements)]
    
    elements.extend(elements)
    
    
    for i in range(n-1):
        for j in range(n):
            sublist = elements[j:j+i+1]
            answer.append(sum(sublist))
    
    answer = len(set(answer))
    
    return answer
