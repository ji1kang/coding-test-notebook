# chapter 4. 구현
# 2022-12-06 22:00 ~ 23:30

# 메모리 사용량: List(int) 
# 1000 = 4KB
# 1,000,000 = 4MB
# 10,000,000 = 40MB

# 4-1 예제: 상하좌우
# 문제정리:
# (N,N) matrix 왼쪽 위부터 좌표시작 (1,1)
# L,R,U,D 좌우상하 이동
# 정사각형 벗어날경우 무시
# 커맨드가 주어지면 도착할 지점의 좌표를 주기

N = 5
query = 'R R R U D D'
x = 1
y = 1 

# 이동횟수가 N번일 경우 시간복잡도는 O(N)
for q in query.split(' '):
    if q == 'U':
        if x - 1 >= 1:
            x-=1
    elif q == 'D':
        if x + 1 <= N:
            x += 1
    elif q == 'L':
        if y - 1 >= 1 :
            y -=1
    elif q == 'R':
        if y + 1 <= N:
            y += 1
    
print(x, y)
        

# 4-2 시각
# 문제정리: 
# int N이 입력되면 00:00:00 ~ N:59:59
# 3이 표함되는 경우의 수

# 문제풀이:
# 시/분/초 60번의 반복필요
# 가장 안좋은 경우의 수를 생각하면 
# 다 돌아버리는 경우 23 * 59 * 59
# 크지 않아서 완전 순회로 풀이

N = 5

freq = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            time = f'{h}{m}{s}'
            if str(time).find('3') > - 1:
                freq += 1
        
print(freq)

# 4-3 왕실의 나이트
# 문제정리: 
# (8,8) matrix
# 나이트의 이동가능한 경우의 수
# (1) x +- 2 -> y +- 1 (오른쪽 왼쪽이 상관없음)
# (2) y +- 2 -> x +- 1
# 정원 밖으로는 갈 수 없음

# 문제풀이:
# 상하좌우를 돌면서 가능한 경우를 찾아봄
# case 1, case 2
# (8,8)로 고정이라 시간 관계없이 짜도 될 듯

input = 'a1'

row = 'abcdefgh'
x = row.index(input[0])
y = int(input[1])

# 가능한 수
steps = [
    (-2,-1),(-2,1),(2,-1),(2,1),
    (-1,-2),(-1,2),(1,-2),(1,2),
]

count = 0
for s in steps:
    dx = x + s[0]
    dy = y + s[1]
    if dx < 1 or dx > 8:
        continue
    if dy < 1 or dy > 8:
    count += 1
    
print(count)
