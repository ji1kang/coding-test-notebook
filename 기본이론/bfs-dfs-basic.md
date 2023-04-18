# 기본설명

- BFS: 정점들과 같은 레벨에 있는 노드들을 먼저 탐색하는 방식 -> 이렇게 해서 넓게 퍼진다
  - 한 단계씩 내
- DFS: 정점의 자식들을 먼저 탐색하는 방식 -> 이렇게 해서 깊이 들어간다
- 그래프 표현 방식: 딕셔너리와 리스트 자료 구조를 활용해서 표현 가능

# BFS (너비 우선 탐색) 알고리즘 구현: 큐를 활용한다 
- 큐큐..큐큐...큐... 너비는 큐.. BBQ..
- 필요한 건 (1) 방문할 큐(need_visit)와 (2) 방문한 큐(visited) 두가지가 필요하다

## 구현하기
1. 가장 먼저 방문할 노드를 방문할 큐에 넣는 것부터 시작한다 (need_visit)
2. 큐니까 FIFO에 따라서 빼내고
3. 꺼낸걸 방문여부를 확인한 뒤 다시 방문한 큐에 넣는다 (visited)
4. 이렇게 한턴이 끝났다

```
grpha = {node: [child...,]}

def bfs(graph, start_node):
  # collections.deque를 써도됨
  need_visited = []
  visited = []
  
  need_visited.append(start_node)
  # 1. 가장 먼저 방문할 노드를 방문할 큐에 넣는 것부터 시작한다 (need_visit)

  while need_visited:
    node = need_visited.pop(0) # 2. 큐니까 FIFO에 따라서 빼내고
    
    if node not in visited:
      visited.append(node) # 3. 꺼낸걸 방문여부를 확인한 뒤 다시 방문한 큐에 넣는다 (visited)
      
      # 4. 이렇게 한턴이 끝났다
      need_visit.extend(graph.get(node, [])) # 4. 다음턴을 생각하며 방금 순회한 노드의 자식 노드를 넣는다
```

```
# 재귀 버전
def dfs(graph, start_node, visited):
    visited[start_node] = True
    print(start_node, end=' ')
    
    for i in graph[start_node]:
        if not visited[i]:
            dfs(graph, i, visited)

```

# DFS (깊이 우선 탐색) 알고리즘 구현: 스택을 활용한다
- 필요한 건 (1) 방문할 스택(need_visit_stack)과 (2) 방문한 큐(visited_queue) 두가지가 필요하다

## 구현하기
1. 가장 먼저 방문할 노드의 자식 노드를 방문할 스택에 넣는 것부터 시작한다 (need_visit_stack) 
2. 스택이니까 FILO에 따라서 맨끝의 노드를 가져온다
3. 꺼낸걸 방문여부를 확인한 뒤 다시 방문한 큐에 넣는다 (visited_queue)
4. 이렇게 한턴이 끝났다


```
grpha = {node: [child...,]}

def dfs(graph, start_node):
  need_visit_stack = []
  visited_queue = []
  
  need_visited.append(start_node)
  1. 가장 먼저 방문할 노드의 자식 노드를 방문할 스택에 넣는 것부터 시작한다 (need_visit_stack) 

  while need_visited:
    node = need_visited.pop() 2. 스택이니까 FILO에 따라서 맨끝의 노드를 가져온다
    # bfs랑 비교해서 여기가 달라졌다
    
    if node not in visited:
      visited.append(node) # 3. 꺼낸걸 방문여부를 확인한 뒤 다시 방문한 큐에 넣는다 (visited)
      
      # 4. 이렇게 한턴이 끝났다
      need_visit.extend(graph.get(node, [])) # 4. 다음턴을 생각하며 방금 순회한 노드의 자식 노드를 넣는다
      
  return visited_stack
```


## 시간 복잡도
- BFS와 DFS 모두: O(num_nodes + num_edges)

