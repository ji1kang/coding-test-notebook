# https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    """
    - log(n) 
    
    - count = []
    
    
    ! 답이 두명이상일 수 있다 - 이때는 오름차순 정렬
    """
    
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0, 0, 0]
    
    for i, a in enumerate(answers):
        if arr1[i % 5] == a:
            count[0] += 1
        
        if arr2[i % 8] == a:
            count[1] += 1
        
        if arr3[i % 10 ] == a:
            count[2] += 1
            
    
    max_val = max(count)
    answer = [i+1 for i, val in enumerate(count) if val == max_val]
    return answer
