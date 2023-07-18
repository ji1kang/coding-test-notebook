import math

def is_prime(x):    #소수 판별 함수
    if x < 2:
        return False
    
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    """
    input: numbers로 주어진 숫자들
    
    1. 주어진 숫자로 만들 수 있는 숫자 찾기
    2. DFS 순회 중에 소수인지 판별되면 정답 처리
    
    + 못풀었던 이유
    - 범위 내의 모든 소수를 찾는 것이 아니라
    - 주어진 숫자가 소수인지만 파악하는 문제
    - 하지만 모든 소수를 찾으려고 해서 문제
    
    
    output: numbers로 만들 수 있는 소수
    """
    max_depth = len(numbers)
    depth = 0
    visited = set()


    def dfs(node, child, depth):
        nonlocal visited
        
        # 정답인지 확인
        if node and int(node) not in visited and is_prime(int(node)):
            visited.add(int(node))

        # 종료 조건 확인
        if max_depth == depth or child == '':
            return # 종료
        else:
            # 다음 노드로 DFS 수행
            for c in child:
                # 맨 마지막의 경우 2의 배수로 끝나면 반드시 소수가 아니다
                if depth + 1 == max_depth and int(c) % 2 == 0:
                    continue
                    
                next_node = node + c
                next_child =  child.replace(c, '', 1)
                dfs(next_node, next_child, depth + 1)
    
    
    dfs('', numbers, depth)
    
    return len(visited)
