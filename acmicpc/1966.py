def gt(x, arr):
    for i in arr:
        if i > x:
            return True
    return False


num_test = int(input())
for _ in range(num_test):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    indices = list(range(n))
    answer = 0

    while queue:
        rank = queue.pop(0)
        index = indices.pop(0)
        
            
        if gt(rank, queue):
            queue.append(rank)
            indices.append(index)
        else:
            answer += 1 # sucess
            if index == m:
                print(answer)
                break
            


# 중요도 큐
# 큐 즁에서... 지금 문서보다 중요한게 있다면
# 지금 문서를 뒤로 보내기
# 주어진 문서가 언제 프린트되는지 리턴
