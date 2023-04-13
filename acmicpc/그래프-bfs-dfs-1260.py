# https://www.acmicpc.net/problem/1260
import sys

lines = sys.stdin.readlines()
n, m, v = list(map(int, lines[0].split(' ')))
from collections import defaultdict, deque
graph = defaultdict(list)

for line in lines[1:]:
	s, t = list(map(int, line.split(' ')))
	if t not in graph[s]:
		graph[s].append(t)
		graph[t].append(s)
		
def dfs(start):
	visited = []
	need_visit = deque([start])
	
	while need_visit:
		node = need_visit.pop()
		if node not in visited:
			visited.append(node)
		
		for child in sorted(graph[node], reverse=True):
			if child not in visited:
				need_visit.append(child)
	
	return visited

def bfs(start):
	visited = []
	need_visit = deque([start])
	
	while need_visit:
		node = need_visit.popleft()
		if node not in visited:
			visited.append(node)
		
		for child in sorted(graph[node]):
			if child not in visited:
				need_visit.append(child)
	
	return visited

print(' '.join(map(str, dfs(v))))
print(' '.join(map(str, bfs(v))))
