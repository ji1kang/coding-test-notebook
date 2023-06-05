# https://school.programmers.co.kr/learn/courses/30/lessons/12936#
def solution(n, k):
    """
    2212 - 2213
    
    20! = 엄청 큼. 시간 복잡도 고려
    - DP 처럼 4!, 3! 사례로 직접해봄
    - 이진트리라고 생각하고 가장 큰 자리 수부터 쳐내는 방식?
    """
    
    answer = []
    # 가능한 숫자
    numbers = list(range(1, n+1))
    
    # 팩토리알 저장 - 계속 사용
    num_child = [1] * (n + 1)
    # num_child[0] = 0
    for i in range(2, n + 1):
        num_child[i] = i * num_child[i-1]
    
    # 자리수를 바꿔 가면서 찾는다
    for i in range(n, 0, -1):
        # i 자리에서 가능한 자식 노드
        child = num_child[i-1]
        
        # 부모 찾기 - 분기로 들어 갈 곳
        parent_index = (k // child)
        if (k % child) != 0:
            parent_index += 1
            
        answer.append(numbers.pop(parent_index - 1))
        
        # k 업데이트
        k -= child * (k // child)  # 이 부분에서 오래 걸렸음
    
    
    
    return answer
