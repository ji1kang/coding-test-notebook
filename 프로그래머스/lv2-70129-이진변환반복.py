# 이진변환 반복하기 (lv-2)
# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 

def solution(s):
    answer = [0, 0]
    
    while True:
        if s == '1':
            break
        else:
            answer[1] = answer[1] + s.count('0')
            s = s.replace('0', '')
            s = bin(len(s))[2:]
            answer[0] += 1
    
    return answer
