# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    """
    22:24 - 22:27
    """
    answer = []
    
    data = {n: s for n, s in zip(name, yearning)}
    
    for arr in photo:
        score = sum([data.get(name, 0) for name in arr])
        answer.append(score)
    
    return answer
