# 18:36 - 19:59
# https://www.acmicpc.net/problem/14891
# 시간이 많이 걸린 이유
# 1. 문제분석에서 집중을 잃어서 한번에 돌리는지 파악이 늦었음
# 2. 필기구 금지 상황의 연습하려다 보니 돌리기 부분에서 헷갈려서 디버깅 오래 걸림
# 이럴 거면 코테 문서에서라도 필기하기

"""Todo
- 회전 결정 필요
- 옆에 있는 톱니바퀴 회전 가능, 회전 안시키는 것도 가능
- 붙은애와 극이 다르면 - 반대로 회전
- 맞닿은 부분의 기준은 회전 방향에 따라 정해짐


돌리는 거 deque 
- -1  반시계면 popleft -> push
- 1 시계면 pop -> pushleft

맞닿은 부분 확인 

1. 3시 방향, 9시 방향 확인 - 2,3인 경우에만 (1,4는 한쪽만)
2. 방향 확인해서 같으면 그쪽 돌려준다 -> 돌려서 옆에도 있으면 확인 후 돌려준다
3. 처음 시작할 때 편하게 생각하려고 그냥 arr를 n+1개로 선언할 걸! 너무 헷갈렸다
"""

import sys
from collections import deque
lines = sys.stdin.readlines()

arr = [deque([int(e) for e in line.strip()]) for line in lines[0:4]]

def rotate(direction, i):
	if direction == 1:
		sn = arr[i].pop()
		arr[i].appendleft(sn)
	else:
		sn = arr[i].popleft()
		arr[i].append(sn)
		

right = 2 # 3시 방향 
left = 6 # 9시 방향

k = int(lines[4])
for i in range(k):
	num, direction = list(map(int, lines[5 + i].strip().split(' ')))
	check = [(num -1 , direction)]
	
	# 오른쪽 확인
	init = num - 1
	init_d = direction
	for other in range(num, 4):
		if arr[init][right] != arr[other][left]:
			check.append((other, init_d * (-1)))
		else:
			break 
		
		init = other
		init_d = init_d * (-1)
			
	# 왼쪽 확인
	init = num - 1
	init_d = direction
	for other in range(num-2, -1, -1):
		if arr[init][left] != arr[other][right]:
			check.append((other, init_d * (-1)))
		else:
			break 
		
		init = other
		init_d = init_d * (-1)
	
	for other, other_d in check:
		rotate(other_d, other)	
			
ans = sum([arr[i][0] * (2 ** (i))  for i in range(0, 4)])
print(ans)
