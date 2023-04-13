# https://www.acmicpc.net/problem/1654
"""
파라메트릭 서치 

- 보통 서치 범위가 엄청나게 클때 (2^31 -1)
- 어떤 조건을 만족하는 위치 중 최대값이나 최솟값을 찾을 때 사용
"""
import sys
k,n = list(map(int, input().split(' ')))
# arr = sorted([int(input()) for _ in range(k)])
arr = sorted([int(sys.stdin.readline()) for _ in range(k)])

max_lan = max(arr)
def calc(mid, arr):
	return sum([lan // mid for lan in arr])


def search(start, end, arr):
	while start <= end:
		mid = (start + end) // 2
		lans = calc(mid, arr)
		
		if lans < n:  
			end = mid -1
		else:
			start = mid + 1
	
	return end # 이 부분이 어려웠음. 어떻게 최대 랜선을 보장하는지?

print(search(1, max_lan, arr))
