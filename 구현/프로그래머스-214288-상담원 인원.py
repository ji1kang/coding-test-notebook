# https://school.programmers.co.kr/learn/courses/30/lessons/214288#

def solution(k, n, reqs):
    from collections import defaultdict
    import heapq as hq
    
    cand = []
    answer = 1e9
    
    k2reqs = defaultdict(list)
    for req in reqs:
        k2reqs[req[-1]].append(req)
        
    
    def dfs(cumsum, path):
        nonlocal cand, n, k
        for i in range(1, (n-k)+2):
            nextsum = cumsum + i
            if nextsum == n and len(path) + 1 == k:
                cand.append(path + [i])
            elif nextsum < n and len(path) + 1 < k:
                dfs(nextsum, path + [i])  
                
    dfs(0, [], n, k)
    
    
    for mentors in cand:
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
