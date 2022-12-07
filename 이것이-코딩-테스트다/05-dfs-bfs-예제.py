# chapter 05. DFS/BFS 이론편
# 2022-12-07 

# 파이썬에서 스택과 큐
# from collections import deque 사용

# 재귀함수 사용시에는 종료조건 달기

# DFS 깊이 우선 탐색
# 인접행렬 -> 메모리 낭비 많음
# 인접리스트 -> 정보 찾기가 귀찮다. 메모리는 효율적.

# DFS는 스택을 사용 
# 멀리있는 노드를 우선적을 탐색
# O(N)

def dfs(graph,v,visited):
    visited[v] = True # 방문노드를 스택에 PUSH
    # 계속 쌓아가는 셈
    # 재귀함수로 구현가능 - 다만 시간이 늦을 수 있다
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
# BFS는 큐를 이용
# 가까운 노드를 우선적으로 탐색
# 여기는 방문노드와 연결된 노드를 큐에 넣고
# 그 다음에 하나씩 꺼내면서 탐색함
# DFS 보다 조금 빠름

from collections import deque

def bfs(graph,start, visited):
    queue = deque([start]) # 방문 노드를 큐에 넣는다
    visited[start] = True # 방문처리
    # 큐가 빌때까지
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
