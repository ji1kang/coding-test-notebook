# https://school.programmers.co.kr/learn/courses/30/lessons/86971
def bfs(start, tree):
    need_visited = [start]
    visited = []
    while need_visited:
        node = need_visited.pop(0)
        visited.append(node)
            
        for child in tree[node]:
            if child not in visited:
                need_visited.append(child)
                
    return len(visited)


def solution(n, wires):
    """
    2130
    
    2150 1차 시도 실패 
    
    - 이걸 트리 형태라고 볼 수 있나?
    """
    from collections import defaultdict
    import copy
    tree = defaultdict(list)
    max_degree_node = 1
    max_degree = 1
    answer = n
    
    for s, t in wires:
        tree[t].append(s)
        tree[s].append(t)


    for root in range(1, n):
        for i in range(len(tree[root])):
            tmptree = copy.deepcopy(tree)
            target_node = tmptree[root].pop(i)
            tmptree[target_node].remove(root)

            cluster1 = bfs(root, tmptree)
            clusted2 = n - cluster1
            
            answer = min(answer, abs(cluster1 - clusted2))
    
    
    return answer
