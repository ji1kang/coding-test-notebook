# 2023-01-11 22:04~22:14
# https://www.acmicpc.net/problem/1439
s=[int(i) for i in input().strip()]


"""
1. 연속이 적을 수록 그리디
2. 연속을 찾는다?
"""

count_ones = 0
count_zeros = 0
last = s[0]

for i in range(1, len(s)):
    if last !=s[i]:
        if last == 1:
            count_ones += 1 
        else:
            count_zeros += 1

    last = s[i]


if last == 1:
    count_ones += 1 
else:
    count_zeros += 1

result = min(count_zeros, count_ones)
print(result)
