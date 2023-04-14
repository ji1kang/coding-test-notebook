# https://www.acmicpc.net/problem/2178
# 2050 2120

import sys
lines = sys.stdin.readlines()
n, m = list(map(int, lines[0].strip().split(' ')))
graph = []
for i in range(n):
	graph.append(
	[int(i) for i in lines[i+1].strip()]
	)
	
"""
1 초 10^2

start (0,0) - (n-1, m-1) # 맨끝
bfs
"""

dx = [0,0,1,-1]
dy = [1,-1,0,0]


need_visit = [(0,0)]
# visit 를 따로 선언 해줬는데 
# 아래에서 neew_visit을 추가할 때 
# 방문한 횟수를 넣어주면 따로 확인할 필요가 없었다

while need_visit:
	x, y = need_visit.pop(0)
		
	if x == (n-1) and y == (m-1):
		break
		
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
			need_visit.append((nx, ny))
			graph[nx][ny] += graph[x][y]
			
print(graph[n-1][m-1])
		
