from collections import deque, OrderedDict

n = int(input())
graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
for i in range(n):
	line = [int(i) for i in input()]
	for j in range(n):
		graph[i][j] = line[j]
		if graph[i][j] == 0:
			visited[i][j] = True
		
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = []

for i in range(n):
		for j in range(n):
			if graph[i][j] == 1 and not visited[i][j]:	
				# serach 
				need_visit = deque([(i, j)])
				count_home = 0
				while need_visit: 
					x, y = need_visit.popleft()
					if not visited[x][y]:
						visited[x][y] = True
						count_home += 1

					# check go?
					for direction in range(4):
						nx = x + dx[direction]
						ny = y + dy[direction]
						if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny] and (nx, ny) not in need_visit:
								need_visit.append((nx, ny))
								


				ans.append(count_home)
				
print(len(ans))
for a in sorted(ans):
	print(a)
				
			
			
		
