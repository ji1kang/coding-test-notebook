"""
# https://github.com/ji1kang/coding-test-notebook/new/main
1 1
2 2
3 3
4 5
5 8
6 13
7 21
8 34
9 55
10 89
11 144
12 233
13 377
14 610
15 987
16 1597
17 2584
18 4181
19 6765

def dfs(cumsum, path):
        nonlocal n, answer
        # 종료 조건
        if cumsum >= n:
            if cumsum == n:
                answer += 1
            return 

        dfs(cumsum + 1, path + '1')
        dfs(cumsum + 2, path + '2')
    
    
    for n in range(1, 20):
        answer = 0
        need_visit = deque([[0, '']])
        count = 0
        while need_visit:
            cumsum, path = need_visit.popleft()
            count += 1
            if cumsum == n:
                answer += 1
                # print(answer, need_visit)

            if cumsum + 1 <= n:
                need_visit.append([cumsum + 1, path + '1'])

            if cumsum + 2 <= n:
                need_visit.append([cumsum + 2, path + '2'])
        print(n, answer)

"""


def solution(n):
    """
    1340 - 1450
    - 처음에 DFS로 풀었다가
    - 100인데도 시간초과 발생 
    - 루프돌면서 규칙성 확인해보니 - DP
    - 점화식으로 변경
    1438
    - 시간초과에서 실패 (n = 60,000일 때는 되는데 왜?)
    - dp로 풀 때 배열로 저장할 필요가 없는데, 불필요하게 저장해서 생기는 문제
    
    output: 채우는 모든 방법의 수
    """
    
    if n <= 2:
        return n
    
    prior1 = 1
    prior2 = 2
    answer = prior1 + prior2
    
    for i in range(3, n+1):
        answer = prior1 + prior2
        prior1 = prior2
        prior2 = answer
        
    return answer % 1000000007
