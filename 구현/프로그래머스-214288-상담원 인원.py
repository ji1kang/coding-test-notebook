# https://school.programmers.co.kr/learn/courses/30/lessons/214288#

def solution(k, n, reqs):
    """
    2126
    2250 1차 시도 - 테스트 8 실패
    """
    from collections import defaultdict
    from itertools import product
    import heapq as hq
    
    k2reqs = defaultdict(list)
    for req in reqs:
        k2reqs[req[-1]].append(req)
        

    answer = 1e9
    
    for mentors in product(range(1, (n-k)+2), repeat = k):
        if sum(mentors) != n:
            continue
        
        wait = 0
        for _type, num_mentors in enumerate(mentors):
            jobs = [0] * num_mentors # 각 멘토별 예상 작업 종료 시간 저장
            _type += 1
            
            for start, vol, _ in k2reqs[_type]:
                fastest_finish_time = hq.heappop(jobs)
                
                if fastest_finish_time <= start:
                    hq.heappush(jobs, start + vol)
                else:
                    wait += (fastest_finish_time - start)
                    hq.heappush(jobs, (fastest_finish_time - start) + start + vol)
        
        answer = min(answer, wait)
    
        
    return answer
