# https://school.programmers.co.kr/learn/courses/30/lessons/159994#
def solution(cards1, cards2, goal):
    """
    1613
    1628 테케 성공
    1640 성공~!
    """
    
    popa = True
    popb = True
    a = ''
    b = ''
    
    
    while goal:
        # 종료조건
        # 1. goal이 없을 때
        # 2. 카드로 못만들 때
        
        if popa and cards1:
            a = cards1.pop(0)
            popa = False
        
        if popb and cards2:
            b = cards2.pop(0)
            popb = False
    
        target = goal.pop(0)
        
        if a == target:
            popa = True
        elif b == target:
            popb = True
        else:
            # 아무 단어도 일치하지 않음 = 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다
            return 'No'
        
    return 'Yes' # goal을 cards1-2로 만들 수 있을 때
