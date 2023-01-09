# 2022-01-09 22:48 ~ 22: 17
# 그리디 문제 

# input
s = [int(token) for token in input()]
n = len(s) 

oper = []
li = list(range(n))

max_result = 0

def calcuate(oper, s):
    cumsum = s[0]
    for o, n in zip(oper, s[1:]):
        if o == '+':
            cumsum+=n
        else:
            cumsum *=n
    return cumsum


while li:
    if len(li) > 1:
        _min, _max = li[0], li[-1]
        o = ['*' for _ in range(_min)] + ['+' for _ in range(_max)]
        max_result = max(calcuate(o, s), max_result)
    
        o = ['*' for _ in range(_max)] + ['+' for _ in range(_min)]
        max_result = max(calcuate(o, s), max_result)
        
        o = ['+' for _ in range(_max)] + ['*' for _ in range(_min)]
        max_result = max(calcuate(o, s), max_result)
        
        o = ['+' for _ in range(_min)] + ['*' for _ in range(_max)]
        max_result = max(calcuate(o, s), max_result)
        
        li.pop(0)
        li.pop(-1)
    else:
        o = ['*' for _ in range(li[0])] + ['+' for _ in range(li[0])]
        max_result = max(calcuate(o, s), max_result)
        
        o = ['+' for _ in range(li[0])] + ['*' for _ in range(li[0])]
        max_result = max(calcuate(o, s), max_result)
        
        oper.append(o)
        li.pop(0)

print(max_result)
