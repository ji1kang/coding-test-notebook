# 2023-01-04 22:02 ~ 22:34
# https://www.acmicpc.net/problem/18428

from itertools import combinations

## 데이터 입력부
n = int(input())

tea = [] # 선생님 위치
stu = [] # 학생 위치
blank = [] # 빈칸 위치
map = [] # 전체맵
for i in range(n):
    line = input().split(' ')
    map.append(line)
    for j in range(n):
        if line[j] == 'T':
            tea.append((i,j))
        elif line[j] == 'S':
            stu.append((i,j))
        elif line[j] == 'X':
            blank.append((i,j))
            
## 풀이과정
# n이 적으니 그냥 순회해도 될거 같은데
# 배치 -> 확인 - 중간에 모두 만족하면 바로 답 도출

def is_exist(map, x, y):
    # 선생님 위치 기준으로 학생확인 
    # 중간에 학생을 한명이라도 발견하면 True
    # 발견실패시 False
    for j in range(y, -1, -1):
        if map[x][j] == 'S':
            return True
        elif map[x][j] == 'O':
            break 
    for j in range(y, len(map), 1):
        if map[x][j] == 'S':
            return True
        elif map[x][j] == 'O':
            break 
    for i in range(x, -1, -1):
        if map[i][y] == 'S':
            return True
        elif map[i][y] == 'O':
            break 
    for i in range(x, len(map), 1):
        if map[i][y] == 'S':
            return True
        elif map[i][y] == 'O':
            break 
    return False



for barrier in combinations(blank, 3):
    # 맵 업데이트 
    for x, y in barrier:
        map[x][y] = 'O'
    
    # 모든 선생에 대해 확인
    for teacher in tea:
        x, y = teacher
        # 학생 발견했을 경우 (True), 숨기 실패 - 내부 루프 탈출
        if is_exist(map, x, y):
            break 
    else: 
        # 탈출 없이 끝날 경우 - 외부 루프 탈출
        print('YES')
        break 
    
    # 맵 원상복귀
    for x, y in barrier:
        map[x][y] = 'X'
    
else: 
    # 외부 루프 한번도 탈출 못할 때
    print('NO')
