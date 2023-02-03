# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 영어 끝말잇기 

def solution(n, words):
    answer = [0,0] # 번호 차례

    data = []
    prev = words[0][0]
    for i, w in enumerate(words):
        if w in data or prev != w[0]:

            break
            
        data.append(w)
        prev = w[-1]
        
    else:
        return [0, 0]
        
    
    answer[0] = ((i+1) % n)
    if answer[0] == 0:
        answer[0] = n
    answer[1] = ((i) // n)+1 
    
    return answer
