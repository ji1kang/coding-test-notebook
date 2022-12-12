# 5 chapter
# 3. 음료수 얼려 먹기
# Todo: 다시 풀기
# 2022-12-12 22:14~22:44

A = ['00100', '00011', '11111', '00000']
A = [[int(item) for item in sublist] for sublist in A]
n = 4
m = 5

def dfs(x,y):
    if x < 0 or x > n -1 or y < 0 or y > n - 1:
        return False
    if A[x][y] == 0:
        A[x][y] = 1
        dfs(x -1, y)
        dfs(x +1, y)
        dfs(x, y + 1)
        dfs(x, y -1)
        # 상하좌우가 모두 존재할 경우 
        return True
    
    # 방문했을 경우
    return False
        
        
count = 0
for row in range(n):
    for col in range(m):
        if dfs(row,col):
            count += 1
print(count)

# 4. 미로탈출
# Todo: 다시 풀기
# 2022-12-12 22:44~22:58
from collections import deque

n=5
m=6
A = ['101010', '111111', '000001', '111111','111111']
A = [[int(item) for item in sublist] for sublist in A]

dx = [-1,1,0,0]
dy =[0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if A[nx][ny] == 0:
                continue
            if A[nx][ny] == 1:
                A[nx][ny] = A[x][y] + 1
                queue.append((nx,ny))
    return A[n-1][m-1]
    
print((bfs(0,0)))
