# 03. 그리디
"""
- 현재 상황에서 지금 당장 좋은 것만 고르는 방법
- 해결책: 최소한의 아이디어로, 해결할 수 있는, 탐욕적인 해결책이 있는지?
"""

# 3-1.py 거스름돈
coins = [500, 100, 50, 10]
N = 1260

for c in coins:
    mod = (N // c) # 몫
    N -= (c * mod) # N %= c 도 가능
    
    # 나머지 
    print(f"{c}원 = {mod}개")
    
# 3-2.py 큰수의 법칙 

# 문제정리:큰수의 법칙 = 배열 수들을 M번 더해서 가장 큰 수를 더함
# 단, 특정 수는 연속 K번 초과해서 더할 수 없음
# 다만 인덱스가 다르면 숫자가 같더라도 더할 수 있음

# 문제풀이: 
# 가장 큰 수를 찾고 -> K 번 더하고 -> 그 다음 큰수를 찾고 -> 한번 더하고 -> 반복
# => 가장 큰수를 최대한 더할 수 있는 횟수를 계산하면 순회를 안해도됨
# 인덱스로 접근해서 같은 수가 존재할 경우에도 문제가 발생하지 않도록 함

N = 5 # an array length
M = 7 # number of addition 
K = 2 # limit of addition

array = [3,4,3,4,3]
array = sorted(array) # array.sort()도 가능

print()
answer = ((array[-1]) * (M // K) * K) + ((array[-2]) * (M % K))
print(answer)

# 3-3.py 숫자 카드게임

# 문제정리: 숫자카드 NxM  (행x열)
# 행(N) 선택 -> 해당행의 가장 낮은 수 뽑음
# 문제 = 최종적으로 가장 높은 숫자를 뽑아야함

# 문제풀이: 역으로 문제를 풀기
# 쉬운 해결책: 순회하면서 가장 높은 수 뽑기

N = 2 # row
M = 4 # col
matrix = []
for _ in range(N):
    matrix.append(input())
    
max_value = 1

for rows in matrix:
    rows = [int(r) for r in rows.split(' ')]
    min_card = min(rows)
    if min_card > max_value:
        max_value = min_card # 한줄로 max(max_value, min_card)로 줄일 수 있음

print(max)

# 3-4.py 1이 될 때까지

# 문제정리: 둘중에 하나만 연산
# (1) N-1 or (2) N / K if N%K==0
# 둘중하나의 연산을 1이 될때 까지 반복
# 단 최소한의 연산으로

# N >= K
N = 17
K = 4

# N % K == 0이 될때까지 (1) 그다음에 (2)

count = 0

while N!=1:
    minus = N % K
    N -= minus
    count += minus
    
    N /= K
    count += 1
    
    if N == 1:
        break
        
    
print(count)