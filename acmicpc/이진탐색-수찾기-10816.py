# https://www.acmicpc.net/problem/10816
import sys
lines = sys.stdin.readlines()

n = int(lines[0])
cards = list(map(int, lines[1].split(' ')))
m = int(lines[2])
targets = list(map(int, lines[3].split(' ')))

## test
# from time import time
# from random import randint
# n = 500000
# m = 500000
# cards = [randint(1, n) for _ in range(n)]
# targets =  [randint(1, n) for _ in range(m)]
# start = time()
##


from collections import Counter
cards = Counter(cards)

ans = [str(cards.get(i, 0)) for i in targets]


print(' '.join(ans))

# print(time() - start)
