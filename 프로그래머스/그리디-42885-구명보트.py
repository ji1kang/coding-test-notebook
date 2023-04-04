# https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    from collections import deque
    people = sorted(people)
    people = deque(people)
    answer = 0
    
 
    
    while people:
        boat = 0
        
        # 최대값 + 최솟값 조합 확인
        # 안돼면
        # 최소값 + 그 다음 최솟값 확인
        # 이렇게 하면 그리디하게 확인 가능
        
        if boat + people[-1] <= limit:
            boat += people.pop()
            if people and boat + people[0] <= limit:
                boat += people.popleft()
        else:
            boat += people.popleft()
            if people and boat + people[0] <= limit:
                boat += people.popleft()
            
        
        answer += 1  
        
    
    return answer
