# https://school.programmers.co.kr/learn/courses/30/lessons/155652
def solution(s, skip, index):
    """
    ! 모두 소문자
    - S를 순회 하면서 바꿔준다
     - 단 z 보다 크면 돌아간다
     - skip도 건너뛴다    
    """

    arr = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
    n = len(arr)
    answer = ''
    
    
    for char in s:
        i = arr.index(char)
        i += index
        if i >= n:
           i %= n
        new_char = arr[i] 
        answer += new_char
    
    return answer
