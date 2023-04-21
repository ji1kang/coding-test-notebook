# https://school.programmers.co.kr/learn/courses/30/lessons/92335
def get_prime(target):
    for i in range(2, int(target ** 0.5) +1):
        if target % i == 0:
            return False
    
    return True

def convert(n, k):
    answer = ''
    
    while n > k:
        n, remain = divmod(n, k)
        answer += str(remain)
     
    answer += str(n)
    return answer[::-1]

def solution(n, k):
    """
    2240 - 1104 - 
    - 1차 시도 1108: 런타임 에러 (일부)
    - 진짜 안찾아져서 봤더니 자료형 문제 인듯 -> 에라토리스 체로하면 너무 문자열이 너무 커지느 문제 발생
    """
    
    # 진법 변환
    nk = convert(n,k) 
    
    # 0 이 아닌 수 골라내기
    arr = [int(num) for num in nk.split('0') if num and num != '1']
    
    # 소수 판단
    answer = 0
    for target in arr:
        if get_prime(target):
            answer += 1
    
    return answer
