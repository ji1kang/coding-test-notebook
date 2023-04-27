# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def is_valid(x, y):
    # 규칙에 맞는지 확인하는 함수
    diff = 0
    for t1, t2 in zip(x, y): # 모든 단어 길이가 같음
        if t1 != t2:
            diff += 1
        
        if diff > 1:
            break
            
    return True if diff == 1 else False


def solution(begin, target, words):
    """2205-2231
    
    """
    # words에 있는 단어로만 변환할 수 있으므로, target을 반드시 포함해야
    if target not in words:
        return 0
    
    # 그래프 생성   
    from collections import defaultdict
    nodes = [begin] + words
    n = len(nodes)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if is_valid(nodes[i], nodes[j]):
                if j not in graph[i]:
                    graph[i].append(j)
                if i not in graph[j]:
                    graph[j].append(i)
    
    # begin_idx -> target_idx 까지의 거리 최단거리 확인
    begin_idx = 0
    target_idx = nodes.index(target)
    answer = -1
    
    need_visit = [begin_idx]
    visit = [False] * n
    while need_visit:
        current_node = need_visit.pop(-1)
        if not visit[current_node]:
            visit[current_node] = True
            answer += 1
            
            # print(nodes[current_node])
            
        if current_node == target_idx:
            break
        
        for child in graph[current_node]:
            if not visit[child]:
                need_visit.append(child)            
        
    
    
    return answer
