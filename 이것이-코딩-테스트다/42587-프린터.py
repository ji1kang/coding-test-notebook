# https://school.programmers.co.kr/learn/courses/30/lessons/42587
#     프린터

def solution(priorities, location):
    # 1. 대기목록 pop(0)
    # 2. 남은 리스트에서 j 보다 높은게 있으면 append()
    # 3. 아니면 스킵
    
    answer = 0
    # 내가 위치한 문서의 인쇄
    while True:
        
        # print(priorities, location)
        now = priorities.pop(0)
        
        
        if max(priorities) > now:
            priorities.append(now)
            # reindex
            if location == 0:
                location = len(priorities) 
        else: 
            answer += 1 # freq print
            if location == 0:
                break
        
        
        
        # move next
        location -=1
        
        
        if len(priorities) == 1:
            answer += 1
            break
        
     
    
    return answer
