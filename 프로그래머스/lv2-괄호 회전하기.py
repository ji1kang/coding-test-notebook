# https://school.programmers.co.kr/learn/courses/30/lessons/76502#

def solution(s):
    """ 0024 - 0050
    
    """
    from collections import deque
    s =  deque([t for t in s])
    n = len(s)
    answer = 0
    
    
    pair = {')': '(', ']': '[', '}':'{'}
    
    for _ in range(n):
        stack = deque()
        
        i = 0
        while i < n:
            if s[i] in [')', ']', '}']:
                if not stack:
                    break
                    
                last = stack.pop()
                if pair[s[i]] != last:
                    break
            else:
                stack.append(s[i])
                
            i += 1
        
        if i == n and not stack:
            answer += 1
            
        
        
        # s를 왼쪽으로 1칸 회전
        first = s.popleft()
        s.append(first)
        
                
    
    return answer
