# https://school.programmers.co.kr/learn/courses/30/lessons/133502
def solution(ingredient):
    """ 0114 - 0136
    빵 - 야채 - 고기 - 빵
    1 2 3 4 5 First In First Out = 큐
    """
    answer = 0
    stack = [ingredient[0]]
    
    for i in range(1, len(ingredient)):
        stack.append(ingredient[i])
        
        if len(stack) >= 4:
            if stack[-4:] == [1,2,3,1]:
                for _ in range(4):
                    stack.pop()
                answer += 1
        
        
            
    
    return answer
