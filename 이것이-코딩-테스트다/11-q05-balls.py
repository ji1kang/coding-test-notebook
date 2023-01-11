#2023-01-11 22:53~22:57

a,b = list(map(int, input().split(' ')))
balls = list(map(int, input().split(' ')))

from itertools import combinations
result = 0
for i, j in combinations(balls, 2):
    if i != j:
        result += 1

print(result)
