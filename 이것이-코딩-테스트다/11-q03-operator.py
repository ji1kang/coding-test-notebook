# 2022-01-09 22:48 ~ 22: 17 (24)
# 그리디 문제 
# tip: 모든걸 탐색할 필요가 없음!!!
# 주어진 조건에서 가장 잘 풀 수 있는 답을 생각

# input
s = input()

cum = 0
for t in s:
    t = int(t)
    if t > 1:
        if cum == 0:
            cum = 1
        cum *= t
    else:
        cum += t

print(cum)
