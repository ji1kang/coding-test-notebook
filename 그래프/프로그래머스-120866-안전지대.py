# https://school.programmers.co.kr/learn/courses/30/lessons/120866#

def solution(board):
    # 1820-1842
    
    n = len(board)
    answer = n * n

    dy = [0, 0, 1, -1, -1,-1, 1, 1]
    dx = [1, -1,0,  0, -1, 1,-1, 1]
    
    safe = [[True for _ in range(n)] for _ in range(n)]
    
    
    for x in range(n):
        for y in range(n):
            # 지뢰
            if board[x][y] == 1:
                
                if safe[x][y]:
                    answer -= 1
                    safe[x][y] = False
                
                # 주변지역
                for d in range(8):
                    ny = dy[d] + y
                    nx = dx[d] + x
                    
                    if 0<=nx<n and 0<=ny<n and safe[nx][ny]:
                        answer -= 1
                        safe[nx][ny] = False
                        
            
    return answer
