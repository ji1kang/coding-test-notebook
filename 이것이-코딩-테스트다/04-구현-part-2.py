# 4-3: 게임개발
# 2022-12-7 22:08 - 22:38

# todo: 해답지와 비교하면서 보면서 리뷰

# 문제정리:  
# 1. 캐릭터 -> 현재방향에서 왼쪽으로 회전 (북동남서 순)
# 2. if 회전방향에 가보지 않은 칸이 있다면 회전한 방향으로 전진 - 왼쪽인덱스를 살펴보기
# 3. if 모든칸을 가봣으면 - 회전만 수행 (1)로 돌아감
# 4. 4번 다 돌고도 모두 가봤거나, 바다로 되어있으면 방향 유지 후 뒤로 
# 단, 바다일경우 스탑!

n = 4
m = 4

x = 1
y = 1
r = 0 # 북

history = [[False] * m] * n

count = 0

maps = []
for _ in range(n):
    maps.append([int(i) for i in input().split()])

while True:
    for trial in range(4): # 4방향 확인
        # 1. 회전
        r += 1
        
        # 2. 전진 
        if r == 0:
            for dy in range(0, y):
                if not history[x][dy]:
                    history[x][dy] = True
                    y -= 1
                    count += 1
                    break
        elif r == 2:
            for dy in range(y, m):
                if not history[x][dy]:
                    history[x][dy] = True
                    y += 1
                    count += 1
                    break
        elif r == 1:
            for dx in range(0, x):
                if not history[dx][y]:
                    history[dx][y] = True
                    x -= 1
                    count += 1
                    break
        elif r == 3:
            for dx in range(y, x):
                if not history[dx][y]:
                    history[dx][y] = True
                    x += 1
                    count += 1
                    break
    
    # 3. 다 확인 or 바다로 되어있을 경우 
    if  trial == 3 or y == 0 or y == m or x == 0 or x == n:
        if r == 0:
            y -= 1
        elif r == 2:
            y += 1
        elif r == 1:
            x -= 1
        elif r == 3:
            x += 1
        
        count += 1
        
        if y == 0 or y == m or x == 0 or x == n or maps[x][y] == 0:
            break


    # cycle
    if r == 3:
        r = 0
        
print(count)
