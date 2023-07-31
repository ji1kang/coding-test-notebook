# https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    """
    2100 - 2129
    
    - 자꾸 TypeError: Object of type set is not JSON serializable 에러가 뜨길래 봤더니
    - set()을 return 하는 과정에서 생기는 문제였음
    
    """
    s = s[1:-1] + ','
    answer = []
    
    for subset in sorted(s.split('},'), key = lambda x: len(x))[1:]:
        outer = set(subset[1:].split(',')) - set(answer)
        answer.append(list(outer).pop(0))
            
    
    return list(map(int, answer))
