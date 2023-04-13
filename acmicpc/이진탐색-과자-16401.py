# https://www.acmicpc.net/problem/16401
import sys
lines = sys.stdin.readlines()

m, n = list(map(int, lines[0].split(' ')))
eats = list(map(int, lines[1].split(' ')))

start = 1
end = max(eats) + 1

while start <= end:
	mid = (start + end) // 2
	
	cuts = sum([t // mid for t in eats if t >= mid])
		
	if cuts < m: # 필요한 과자 수보다 잘라서 남은 과자 수가 적을 경우 
		# = 잘라야하는 과자의 길이가 너무 길다
		# = 과자의 길이를 줄인다 = 왼쪽 탐색
		end = mid - 1
	
	else:
		start = mid + 1 # 오른쪽 탐색
		
	
end = 0 if end == max(eats) + 1 else end
print(end)
	
