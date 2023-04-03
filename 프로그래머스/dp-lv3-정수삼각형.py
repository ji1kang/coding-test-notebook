# 50분
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    n = len(triangle)
    dp = [[None] * (n) for _ in range(n)]
    for i in range(n):
        dp[i][:i+1] = triangle[i]
    
    for i in range(1, n):
        for j in range(i + 1):
            tmp = []
            
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + dp[i][j]
            else:
                dp[i][j] = max(dp[i][j] + dp[i-1][j-1], dp[i][j] + dp[i-1][j])
    
    answer = max(dp[-1])
    return answer
