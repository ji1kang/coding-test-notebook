"""
- 활용처

1. 서로소 집합
2. 무방향 그래프 내에서의 사이클 판별 (방향 그래프의 경우 DFS)
3. 신장 트리 (하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분의 그래프)
4. 크루스칼 알고리즘 (ex. 최소비용으로 도시를 연결하는 다리 만드는 문제)
  1) 간선 데이터를 비용에 따라 오름차순으로 정렬
  2) 간선을 하나씩 확인하면서 현재의 간선이 사이클을 발생시키는지 확인
  - 사이클이 발생 = 최소 신장 트리 포함
  - 사이클이 발생하지 않음 = 최소 신장 트리에 포함 X
  3) 모든 간선에 대해서 2)의 과정을 반복
  * 트리구조는 노드가 N개일 때 간선의 갯수가 N-1
  
"""
# * 관련문제 - https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 각 노드별로 부모 테이블을 선언할 경우의 알고리즘

def find_parent(parent, x):
  """
  # 경로 압축 기법을 활용해 변경 가능
  # 시간복잡도는 O(V+M(1+log_{2-M/N}V), 대략 천개의 노드에 대해서 천만번 수행
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x] # parent[x] 경우는 parent[x] == x 이므로, 아닐 경우에는 재귀함수 수행
  """
  # 루트 노드가 아니라면 x의 부모의 부모를 재귀적으로 찾아가도록 구성
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

def solution(n, costs):
    answer = 0
    edges = 0
    
    parent = list(range(n))
    costs.sort(key = lambda x: x[2])
    
    for v, s, cost in costs:
        if find(v, parent) != find(s, parent):
            union(parent[v], parent[s], parent)
            answer += cost
            edges += 1
    
        if edges == n - 1: # 이 부분에서 오류! 최소 신장 트리에 포함되는 간선의 갯수는 노드 - 1
            break
            
    return answer
