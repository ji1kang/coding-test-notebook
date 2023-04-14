# 11:13 - 12:03 (48)
import sys
lines = sys.stdin.readlines()
n = int(lines[0])
arr = []
for i in range(n):
	v, w = lines[i+1].strip().split(' ')
	arr.append((int(v), int(w) * -1, (i+1) * -1) )
# 배열 정렬시 i-1 번째 인덱스 값 같을 경우 i 번째 인덱스가 낮은 순으로 정렬되는 걸 이용


arr = sorted(arr)

init = arr[0]
ans = init[-1] * (-1) # 결승선 차량 번호의 합
for i in range(1, n):
	# 여기서 변수 지정하는 부분에서 시간초과가 났는데
	# 아마 변수 지정 과정에서 시간이 걸려서 그런듯
	# 필요한 경우가 아니라면 시간 빡빡 할때는 가독성 등을 위해 쓸모없는 변수 지정 하지말 것
	if init[0] != arr[i][0]:
		ans += arr[i][-1] * (-1)
		init = arr[i]

print(ans)
