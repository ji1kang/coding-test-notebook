def solution(prices):
    """
    2220
    
    1. 입력
    - 2 <= len <= 10^5 : O(NlogN)
    
    3. 출력
    - 가격이 떨어지지 않은 기간 (초)
    
    2256
    +_+ 한번에 성공
    
    사용한 케이스
    [5, 4, 3, 2, 1] - [1, 1, 1, 1, 0]
    [1, 1, 1, 1, 1] - [4, 3, 2, 1, 0]
    [1] * 10000
    """
    answer = [0] * len(prices)
    num_prices = len(prices)
    
    queue = []
    for i in range(num_prices):
        
        while queue:
            # (배열 있으면) 마지막 애랑 비교
            # 만약 마지막애가 더 크면 = 가격이 떨어짐
            # 같거나 작은애를 만날 때 까지  큐를 pop 하면서 떨어지지 않은 기간 구하기
            if queue[-1][0] > prices[i]:
                last_price, last_index = queue.pop()
                answer[last_index] = i - last_index 
            else:
                break
        queue.append((prices[i], i)) # 가격과 인덱스 줄세우기
        
    while queue:
        # 남은 큐 = 떨어져본적이 없는 애들
        # 떨어지지 않은 기간 = 전체 길이 - 자기 인덱스
        last_price, last_index = queue.pop()
        answer[last_index] = num_prices - last_index - 1
    
    
    return answer
