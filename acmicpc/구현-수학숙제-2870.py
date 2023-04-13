import sys
n = int(input())
lines = sys.stdin.readlines()

"""
01. 숫자 찾기
02. 숫자를 비 내림차순 정렬
03. 숫자의 앞에 0이 있을 때는 생략
- 03 이면 3
"""

import re
ans = []

for line in lines:
	groups = re.findall(r'\d+', line)
	groups = [int(g) for g in groups]
	ans.extend(groups)
	
print(
	'\n'.join(
		list(map(str, sorted(ans)))
	)
)
	
