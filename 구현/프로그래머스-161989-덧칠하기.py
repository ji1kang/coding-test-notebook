# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    """
    2133 - 2154
    
    output: 페인트칠의 최적화
    """
    answer = 1
    
    start_area = section.pop(0)
    
    for area in section:
        if area - start_area >= m:
            # m 롤러로 start ~ area까지 칠할 수 없을 때
            answer += 1
            start_area = area
        else:
            # m 롤러로 start ~ area까지 칠할 수 있을 때
            pass
    
    return answer
