def solution(n, lost, reserve):
    """
    ! 번호는 체격 순 = 앞뒷 인덱스만 가능
    ! 목적 = 최대한 많이 빌려주기
    ! 여벌이 있지만 도난당하면 못빌려줌
    
    - 배열 초기화 + 답 초기화
    - LOST 반복하면서 가능한지 확인 + 가능하면 + 1
    """
    answer = n - len(lost)
    
    remain = [1 if i in reserve  else 0 for i in range(n+1)]
    
    for i in sorted(lost): # 정렬이 보장되어 있는지 확인
        if remain[i] == 1:
            answer += 1
            remain[i] = 0
        
        elif remain[i-1] == 1 and i-1 not in lost: # 현재만 확인해야하는지? 아니면 다른것도 확인해야하는지 확인
            answer += 1
            remain[i-1] = 0
            
        elif i+1 <= n :
            if remain[i+1] == 1 and i+1 not in lost:
                answer += 1
                remain[i+1] = 0

    
    return answer # 최대 체육 참여자
