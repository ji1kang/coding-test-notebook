# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def collatz(k):
    # 로타르 콜라츠(Lothar Collatz) 실행
    result = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = (k * 3) + 1
            
        result.append(k)
    return result

def integral(x1, x2, y):
    area = 0
    
    for x in range(x1, x2 - 1):
        
        y1 = y[x]
        y2 = y[x + 1]
        
        max_h = max(y1, y2)
        w = 1
        min_h = abs(y1 - y2)

        square_area = max_h * w
        tri_area = (min_h * w) / 2
        
        area += (square_area - tri_area)
    
    return area

def solution(k, ranges):
    """
    2105 - 2146
    
    Todo
    1. 수열 함수 작성
    2. 정적분 수행: integral
    """
    answer = []
    y = collatz(k)
    n = len(y)
    
    for a, b in ranges:

        # 1. [0,0] 구간
        if a == b == 0:
            #  이를 [0,0] 구간에 대해 정적분 한다면 전체 구간에 대한 정적분이며
            answer.append(integral(a, len(y), y))
            print(a, b)
            continue
        
        # 2. b가 0 또는 음수라면 [a, b]에 대한 정적분 결과는 x = a, x = n - b
        if b <= 0:
            b = n + b 
        
        # 3. 정적분 수행
        if a >= b:
            # 3 - 1. 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어질 수 있으며 이때의 정적분 결과는 -1로 정의합니다.
            answer.append(-1)
        else:
            # 3 -2. 보통의 경우
            answer.append(integral(a, b, y))
    
    
    return answer
