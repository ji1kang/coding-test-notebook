def solution(operations):
    """2216 - 2223
    10^6 - 확인
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333", "I 333"] * 100000
    
    1st - 히든테케 하나 틀림
    2nd - 마지막에 정렬 안해줘서 그럼 - heappush인데 정렬이 왜 또 필요하지?
    * 힙의 마지막 인덱스가 가장 큰값이라는 보장이 없음
    * 그렇다면 pop을 수행할때도 문제가 생김 -> heapq 사용 보다 직업 만드는 게 확실
    """
    
    
    import heapq as hq
    answer = []
        
    for ops in operations:
        cmd, num = ops.split(' ')
        num = int(num) 
        
        if cmd == 'I':
            hq.heappush(answer, num)
        
        elif cmd == 'D' and answer:
            if num == -1:
                hq.heappop(answer)
            elif num == 1:
                answer.pop(-1)
    
    
    if answer:
        answer = sorted(answer)
        return [answer[-1], answer[0]]
    else:
        return [0, 0]
