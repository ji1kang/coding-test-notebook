# https://school.programmers.co.kr/learn/courses/30/lessons/172928
def solution(park, routes):
    # 21:50 - 22:14
    answer = []
    
    # 지도 정의
    maps = []
    for i, p in enumerate(park):
        row = []
        for j, t in enumerate(p):
            # 시작점 표시
            if t == 'S':
                start = (i, j)
            
            # 장애물 표시
            if t == 'X':
                row.append(-1)
            else: # 'O'
                row.append(0)
        maps.append(row)
        
                
    # 라우트 이동
    for r in routes:
        d, step = r.split(' ')
        
        nx, ny = start
        cond = True # 조건해당?
        for _ in range(int(step)):
            dx, dy = nx, ny
            if d == 'E':
                dy += 1
            elif d == 'W':
                dy -= 1
            elif d == 'S':
                dx += 1
            else:
                dx -= 1

            # 이동 조건 확인
            if 0 <= dx < len(maps) and 0 <= dy < len(row) and maps[dx][dy] != -1:
                nx, ny = dx, dy
            else:
                cond = False
                break
        
        if cond:
            start = [nx, ny]
    
    
    return start
