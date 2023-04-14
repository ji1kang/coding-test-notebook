# 10:39 - 11:08
import sys
lines = sys.stdin.readlines()
n = int(lines[0])
arr = [int(s) for s in lines[1].strip().split(' ')]

ans = arr[0]
cumsum = arr[0]

for i in range(1, n):
	if arr[i] - arr[i-1] == 1:
		cumsum += arr[i]
	else:
		cumsum = arr[i]

	ans = max(cumsum, ans, arr[i])

print(ans)

"""
테케 중에 런타임에러가 자꾸나서 애먹었던 문제
문제는 하나 밖에 없을 때는 strip()처리가 안되었던 문제였음
1
100
"""
