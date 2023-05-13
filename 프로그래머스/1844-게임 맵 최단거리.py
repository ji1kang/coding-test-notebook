# https://school.programmers.co.kr/learn/courses/30/lessons/1844#
def solution(maps):
    from collections import deque
    answer = -1
    n = len(maps)
    m = len(maps[0])
    start = (0,0)
    end = (n-1, m-1)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    # case 1: 상대 팀 진영에 도착할 수 없을 때
    check = 0
    
    for d in range(4):
        nx = end[0] + dx[d]
        ny = end[1] + dy[d]

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
            check =+ 1
            
    if check == 0:
        return -1
    
    # case 2: 상대 팀 진영에 도착할 수 있을 때
    need_visit = deque([start])
    
    while need_visit:
        node = need_visit.popleft()
        if node == end:
            return maps[node[0]][node[1]]
            
        for d in range(4):
            nx = node[0] + dx[d]
            ny = node[1] + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] += maps[node[0]][node[1]]
                need_visit.append((nx, ny))
            
    return answer
