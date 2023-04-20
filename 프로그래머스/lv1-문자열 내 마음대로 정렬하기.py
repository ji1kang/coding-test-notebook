def solution(strings, n):
    """ 0007 - 0022
    조건 - 각 문자열의 n번째 글자를 기준으로 오름차순으로 정렬
       
    """
    answer = sorted(sorted(strings), key = lambda x: x[n])    
    
    return answer
