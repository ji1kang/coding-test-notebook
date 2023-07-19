# https://school.programmers.co.kr/learn/courses/30/lessons/120860

def solution(dots):
    
    dots = [[256 + x, 256 + y] for x, y in sorted(dots)]
    print(dots)
    
    
    w = dots[2][0] - dots[0][0]
    h = dots[1][1] - dots[0][1]
    
    
    return w * h
