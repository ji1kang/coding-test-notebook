n = int(input())
arr = [int(input()) for _ in range(n)]


for i in range(n):
    for j in range(i, 0, -1):
        if arr[j] > arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]

print(arr)


====

n = int(input())
arr = [input().split(' ') for _ in range(n)]
arr = [(k, int(v)) for k, v in arr]

sorted(arr, key = lambda x: x[1])
for a in arr:
    print(a[0], end=' ')

====

n, k = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
