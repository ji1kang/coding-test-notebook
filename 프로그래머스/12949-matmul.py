# https://school.programmers.co.kr/learn/courses/30/lessons/12949
def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    
    answer = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row): # row
        for j in range(col):
            tmp = 0
            for a,b in zip(arr1[i], [sublist[j] for sublist in arr2]):
                tmp += (a * b)
            answer[i][j] = tmp

        
    
    return answer
