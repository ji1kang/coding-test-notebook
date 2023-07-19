# https://school.programmers.co.kr/learn/courses/30/lessons/159993#

def bfs(start, end, points, maps):
    need_visit = [points[start]]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n, m = len(maps), len(maps[0])
    
    while need_visit:
        x, y = need_visit.pop(0)

        if [x, y] == points[end]:
            return maps[x][y] - 1
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny <m and maps[nx][ny] == 1:
                need_visit.append([nx, ny])
                maps[nx][ny] += maps[x][y]
    
    return 0


def solution(maps):
    import copy
    
    answer = 0
    
    points = {} # S, E, L
    for i in range(len(maps)):
        tmp = []
        for j, char in enumerate(maps[i]):
            if char == 'X':
                tmp.append(0)
            else:
                tmp.append(1)
            
            if char in ['S', 'E', 'L']:
                points[char] = [i, j]
                
        maps[i] = tmp
    
    to_L = bfs('S','L', points, copy.deepcopy(maps))
    
    if to_L == 0:
        return -1
    
    to_E = bfs('L','E', points, copy.deepcopy(maps))
    
    if to_E == 0:
        return -1
    
    return to_L + to_E
