# https://www.acmicpc.net/submit/2805
import sys
lines = sys.stdin.readlines() # 이거 쓰면 입력값 한번에 받아옴 '\n'이 포함될 수 있음

n, m = list(map(int, lines[0].split(' ')))
arr = list(map(int, lines[1].split(' ')))
# arr를 sort할 필요 없음 = 우리가 찾는 건 연속된 높이 배열 내에 존재

# 찾는 값의 범위 설정
start = 1
end = max(arr) + 1 

while start <= end:
		mid = (start + end) // 2
		
		cut = sum([t - mid for t in arr if t> mid])
				
		if cut == m:
			end = mid
			break
		elif cut < m: # 절단값이 m 보다 작은 경우 = 높이를 줄여야 함 = 왼쪽 탐색 (작은 구간)
			end = mid - 1
		else: # 절단값이 m 보다 큰 경우 = 높이를 올려야 함 = 오른쪽 탐색 (큰 구간)
			start = mid + 1 # 이 부분 오타로 계속 시간 초과 떳었다..
      
print(end)
