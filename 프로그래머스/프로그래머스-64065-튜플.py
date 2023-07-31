# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    """
    2100 - 2129
    
    - 자꾸 TypeError: Object of type set is not JSON serializable 에러가 뜨길래 봤더니
    - set()을 return 하는 과정에서 생기는 문제였음
    
    """
    s = s[1:-1] + ',' # 문자열 다루기 편하게 변환해줌
    answer = []
    
    for subset in sorted(s.split('},'), key = lambda x: len(x))[1:]:
        for item in map(int, subset[1:].split(',')):
            if item not in answer:
                answer.append(item)
                break
    
    return answer
