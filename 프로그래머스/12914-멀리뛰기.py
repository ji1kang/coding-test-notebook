def solution(n):
    """
    n = 1...n까지 직접해보면 알 수 있음
    2216 1차 시도 실패
    2218 인덱싱 헷갈려서 그런거였음 ㅠㅠ
    """
    
    arr = [0] * (n+2)
    
    arr[1] = 1
    arr[2] = 2
    
    if n > 2:
        for i in range(3, n+2):
            arr[i] = arr[i-1] + arr[i-2]
    
    return arr[n] % 1234567
