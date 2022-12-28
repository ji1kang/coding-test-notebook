# 2022-12-28 22:16
# TODO: 다음엔 직접 풀어보자
# TODO:
# 내장툴사용해서 해보기
# import itertools
# it = itertools.combinations(zero, 3)
"""
2000110
0010120
0110100
0100000
0000011
0100000
0100000
"""



n,m=7,7
graph = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    row = input().split()
    graph.append(row)
    
print(graph)
    

# 이동하므로
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx >=0 and nx < n and ny >=0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(x,y) # 재귀적으로 작동해서 확산을 표현

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score +=1
                
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                # 맵 복붙 
                temp[i][j] = graph[i][j]
        # 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        result = max(result, get_score())
        return 
    # 순회하면서 빈벽세우기 
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1
                    
dfs(0)
print(result)

# 2 <= num_2 < 10 -- 범위가 작으니까 그냥 순회해도 되나?
# 경우의 수 모든 맵에서 1을 세울 수 있는 모든 경우의 수 확인
# 1을 먼저 3개 채워야함 

# 문제를 쪼개서 생각하기
# 조건 1. 벽을 세개 세워야함
# 조건 2. 해당 벽을 기준으로 바이러스가 갈 수 있는 범위 확인 -> 0으로 연결된 component 확인 -> dfs가 적합
