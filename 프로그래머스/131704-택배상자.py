# https://school.programmers.co.kr/learn/courses/30/lessons/131704
# 2215 - 2251
def solution(order):
    from collections import deque
    """
    order 10^6
    1...n -> order -> 정렬
    보조 컨테이너 stack - 짐을 두는 곳
    메인 컨테이너 queue
    """
    answer = 0
    order = deque(order)
    main = deque(range(1, len(order) + 1))
    sub = deque([None])
    
    box = order.popleft() # 첫상자 빼기
    
    
    # 벨트 업데이트 - 첫상자 만날 때까지
    while True: # TODO: 추후 변경
        # 상자를 못찾았을 때
        if main and box > main[0]:
            if main: 
                move = main.popleft()
                sub.append(move)
        # 상자를 찾았을 때
        elif main and box == main[0]:
            answer += 1
            if main: 
                main.popleft()
            if order:
                box = order.popleft()
        elif sub and box == sub[-1]:
            answer += 1
            if sub:
                sub.pop()
            if order:
                box = order.popleft()
        else:
            break        
    
    return answer
