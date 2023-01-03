"""
2023-01-03
22:20~23:00
https://www.acmicpc.net/problem/14888
[제약]
- 수의 순서는 고정
- 연산자 우선순위는 무시
o - 나눗셈은 몫만 취함
o - 음수를 양수로 나눌 때는 - 양수로 바꾼 뒤 몫을 취하고 다시 음수
[문제]
- 최대와 최소
"""

n = input()
arr = list(map(int, input().split(' ')))
op = list(map(int, input().split(' ')))
oper = []
for i in range(4):
    if i == 0:
        for _ in range(op[i]):
            oper.append('+')
    elif i == 1:
        for _ in range(op[i]):
            oper.append('-')
    elif i == 2:
        for _ in range(op[i]):
            oper.append('*')
    elif i == 3:
        for _ in range(op[i]):
            oper.append('/')

max_result = -1000000000
min_result = 1000000000

def divide(x,y):
    if x < 0 and y > 0:
        x = x * -1
        result = (x // y) * -1
    else:
        result = (x // y)
    return result
        
from itertools import permutations

# Todo: dfs로 푸는 방법도 존재함
for operations in set(permutations(oper)):
    result = arr[0]
    
    for n, o in zip(arr[1:], operations):
        if o == '+':
            result = result + n
        elif o == '-':
            result = result - n
        elif o == '*':
            result = result * n
        elif o == '/':
            result = divide(result, n)
        
    max_result = max(max_result, result)
    min_result = min(min_result, result)
     
    
print(max_result)
print(min_result)
