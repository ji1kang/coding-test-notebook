#https://school.programmers.co.kr/learn/courses/30/lessons/154540#

def solution(maps):
    """
    2104
    
    2130 1차 시도 실패??
    2141 변수 겹쳐서 그런거였음. 변수명 헷갈리지 않게 잘 짓자..
    """
    answer = []
    n, m = len(maps), len(maps[0])
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    
    for i in range(n):
        for j in range(m):
            
            if maps[i][j] != 'X' and not visited[i][j] :
                
                need_visit = [(i, j)]
                visited[i][j] = True
                cost = int(maps[i][j])
                
                while need_visit:
                    y, x = need_visit.pop(-1)
                    
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X' and not visited[ny][nx]:
                            visited[ny][nx] = True
                            need_visit.append([ny, nx])
                            cost += int(maps[ny][nx])
                    
                
                answer.append(cost)
            
    
    
    
    return sorted(answer) if answer else [-1]
