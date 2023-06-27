# https://school.programmers.co.kr/learn/courses/30/lessons/154538
def solution(x, y, n):
    """09:00-09:33
    10^6
    
    x -> y 최소 횟수
    연산은 3번만 가능
    
    2,3을 곱해서 y가 되려면
    y가 2,3의 배수여야 함
    
    역순으로 가서 트리 형태로 풀이
    
    1트라이 3테스트 케이스 실패 9:08
    2트라이 2테스트 케이스 실패 9:18
    성공! 9:33 테케 세번째의 경우는 depth 모두에서 발생하는 문제이므로 조건을 잘못채워서 생긴 문제였음
    """
    answer = 0
    
    # 엣지 케이스
    if x == y:
        return answer

    # BFS
    need_visit = [y]
    
    while need_visit:
        answer += 1
        next_nodes = []
        
        # depth 순회
        for node in need_visit:
            # 연산 1
            if node > n: # x는 0이 될 수 없으므로
                tmp = node - n
                if tmp == x:
                    return answer
                elif tmp > x:
                    next_nodes.append(tmp)
            
            # 연산 2
            if node % 2 == 0:
                tmp = node // 2
                if tmp == x:
                    return answer
                elif tmp > x:
                    next_nodes.append(tmp)
            
            # 연산 3
            if node % 3 == 0:
                tmp = node // 3
                if tmp == x:
                    return answer
                elif tmp > x:
                    next_nodes.append(tmp)
                    
        if not next_nodes: # 깊
            return -1
        
        need_visit = next_nodes
        
    
    return answer
