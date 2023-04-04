# https://school.programmers.co.kr/questions/42879

def solution(n,a,b):
    
    # 계산 편의를 위해 짝수로 만들어줌
    
    answer = 1
    # range 0부터 시작할 경우 (1,2)은 커버가 안돼서 1부터 시작
    for i in range(1, n // 2): # 최대 실행 횟수는 n // 2
        if (b - a  == 1 or b - a == -1) and (a//2 != b //2)  :
            break
        else:
           
            a = (a//2) + 1 if a % 2 == 1 else (a//2)
            b = (b//2) + 1 if b % 2 == 1 else (b//2)
            
            answer += 1
    


    return answer
