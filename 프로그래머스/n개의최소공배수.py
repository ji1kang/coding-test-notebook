# https://school.programmers.co.kr/learn/courses/30/lessons/12953#
def solution(arr):
    if len(arr) == 1:
        return arr[0]
    
    def lcm(a, b):
        lcm = max(a, b)
        while True:
            if lcm % a == 0 and lcm % b == 0:
                return lcm
            lcm += 1
    
    
    
    arr = sorted(arr)
    
    answer = arr[0]

    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
        
    return answer
