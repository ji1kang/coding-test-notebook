# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    """
    2200 - 2221
    
    # input
    - 순서는 고정
    - 타켓 넘버를 만드는 *모든 방법* 찾기
    - 연산은 +/- 만 가능
    
    # solve
    - 루트를 0으로 두고 다음 depth 마다 +(다음숫자), -(다음숫자)가 추가되는 이진트리로 생각
    - BFS로 맨 마지막 depth의 노드들을 구한 후
    
    # output
    - 마지막으로 target과 일치하는 노드의 갯수를 세면 됨
    """
    n = len(numbers)
    
    need_visit = [0] # root
    
    for depth in range(1, n+1):
        child = []
        for node in need_visit:
            child.append(node + numbers[depth - 1])
            child.append(node - numbers[depth - 1])
            
        need_visit = child
            
    answer = sum([1 for node in need_visit if node == target])
            
            
    return answer
