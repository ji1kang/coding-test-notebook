# https://school.programmers.co.kr/learn/courses/30/lessons/135808
def solution(k, m, score):
    """
    ! 상자에 못담는 건 버림
    1,000,000 = nlog
    """

    n = len(score)
    score = sorted(score, reverse=True)
    num_box = n // m
    score = score[:min(n, num_box * m)]
    n = len(score)
    
    answer = 0 # 이익이 없는 경우

    for i in range(n-1, -1, -1 * (m)):
        answer += (score[i] * m) 
        
        
    return answer
