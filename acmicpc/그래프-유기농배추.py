# https://www.acmicpc.net/problem/2178
# 2125 2202

"""
foold fill
"""

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(i, j):
	need_visit = [(i, j)]
	graph[i][j] = 0 # 방문처리

	while need_visit:
		x, y = need_visit.pop(0)

		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]

			if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
				need_visit.append((nx, ny))
				graph[nx][ny] = 0 # 이제 방문은 필요 없으니까!

t = int(input())
for i in range(t):
	m, n, k = list(map(int, input().strip().split(' ')))
	
	# graph 생성
	graph = [[0] * n for _ in range(m)]
	for _ in range(k):
		x, y = list(map(int, input().strip().split(' ')))
		graph[x][y] = 1
	
	# 액션
	ans = 0 # 벌레
	for i in range(m):
		for j in range(n):
			# dfs
			if graph[i][j] == 1:
				ans += 1 # 시작 
				dfs(i, j)
				
							
	print(ans) 
		
