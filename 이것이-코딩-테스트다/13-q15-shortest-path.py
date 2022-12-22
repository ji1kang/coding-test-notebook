# 2022-12-22 15:16 ~ 15:55
# 15. 특정 거리의 도시 찾기
from collections import deque

n,m,k,x=map(int, input().split(' '))
# 도시, 도로, 거리, 출발
# Q. 출발노드로 부터 최단거리 k에 있는 노드를 출력
# 최단거리 -- bfs로 구하기

graph = {}

for _ in range(m):
    s, t = map(int, input().split(' '))
    if s !=t:
        child = graph.get(s, [])
        child.append(t)
        graph[s] = child
        
answer = []
visited = [False] * (n+1) 


def bfs(graph, start, visited):
    q = deque([(start, 0)]) # 큐를 생성

    while q:
        v, w = q.popleft() # 방문할 노드 찾기
        visited[v] = True # 방문 표시       
        
        if w == k: # 최단거리 k 이상인 노드는 찾을 필요 없음
            answer.append([v,w])
            
        for child in graph.get(v, []): # v와 연결된 노드 순회
            if not visited[child]:
                q.append((child, w+1))
                visited[child] = True 
            
bfs(graph, x, visited)
if answer:
    for v, w in answer:
        print(v)
else:
    print(-1)

