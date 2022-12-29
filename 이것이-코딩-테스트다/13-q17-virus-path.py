# 2022-12-29 22:37 ~ 23:28
# q.17 경쟁적 전염
# https://www.acmicpc.net/problem/18405

# (1) 문제정리

# n,n 시험관
# 1~k 바이러스
# 바이러스는 상,하,좌,우로 1초마다 증식
# 낮은 것부터 증식
# 한칸에는 하나의 바이러스만

# given
# 시험관의 크기와 바이러스의 위치 정보
# S초가 지난 후에 x,y에 존재하는 바이러스의 종류 출력
# 없으면 0

# (2) 가장 나이브한 

n,k=list(map(int, input().split(' ')))
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split(' '))))
    
s,x,y=list(map(int, input().split(' ')))
x -=1
y -=1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def move(x,y,virus,graph):
    for i in range(4): # 상하좌우
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >=0 and ny < n:
            if graph[nx][ny] == 0: # 바이러스는 선착순
                graph[nx][ny] = virus
                
    return graph 
            
from copy import deepcopy
for count in range(s):
    # 1. 이동 함수 구현
    # 2. 낮은 수부터? - 가장 나이브한 방법 순회? - 여기서 이미 상하좌우 간애만 표시해서 중복 연산 줄이기
    # 200 * 200 * 1000 * 10000 = 400,000,000,000 
    # 3. 끝은 어떻게?
    for virus in range(1, k+1):
        tmp = deepcopy(graph)
        for i in range(n):
            for j in range(n):
                if graph[i][j] == virus:
                    tmp = move(i,j,virus,tmp)
                    print(i,j,virus, graph)
        # update
        graph = tmp
        
print(graph[x][y])


# (3) 머리를 써보자!
# 위의 경우는 정답은 맞지만 시간 초과 -> 
# 순회대신 너비우선탐색 (***큐***,bfs를 써보자)

from collections import deque

n,k=list(map(int, input().split(' ')))
graph = []
virus = []
for i in range(n):
    row = list(map(int, input().split(' ')))
    graph.append(row)
    
    for j in range(n):
        if row[j] !=0:
            virus.append((row[j],0,i,j))
    
s,x,y=list(map(int, input().split(' ')))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

virus.sort()
q = deque(virus)


while q:
    v,now,vx,vy = q.popleft()
    if now == s:
        break
    for i in range(4): # 상하좌우
        nx = vx + dx[i]
        ny = vy + dy[i]
        if nx >= 0 and nx < n and ny >=0 and ny < n:
            if graph[nx][ny] == 0: # 바이러스는 선착순
                graph[nx][ny] = v
                q.append((v,now+1,nx,ny))

print(graph[x-1][y-1])
