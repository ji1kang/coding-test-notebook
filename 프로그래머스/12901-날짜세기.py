https://school.programmers.co.kr/learn/courses/30/lessons/12901?language=python3#

def solution(a, b):
    """
    todo
    - a - 1월까지의 날짜 세기
    - b를 더해주기
    
    ! 홀수달  30 
    ! 2월 29
    ! 짝수달 31
    """
    # init
    days = [ 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    answer = 6
    
    # month
    if a  > 1:
        for i in range(1, a):
            if i in [1, 3, 5, 7, 8, 10, 12]:
                answer += 31
            elif i == 2: # 여기서 실수가 있었음
                answer += 29
            else:
                answer += 30
   

    # day
    answer += b
    answer %= 7
    return days[answer]
    
    
    
