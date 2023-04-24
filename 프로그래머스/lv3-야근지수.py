def index(arr):
    return sum([(a * -1) ** 2  for a in arr])

def solution(n, works):
    """ 2244 - 2256 - 2258
    work += (end-start) ** 2
    n = 10^6 -> nlogn?
    
    """
    import heapq as hq
    
    works = [w * -1 for w in works]
    hq.heapify(works)
    
    for t in range(n):
        if works:
            max_job = hq.heappop(works)
        if max_job !=0:
            hq.heappush(works, max_job + 1)
    
    answer = index(works)
    return answer
