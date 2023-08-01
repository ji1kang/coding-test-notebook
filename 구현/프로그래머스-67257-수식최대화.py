# https://school.programmers.co.kr/learn/courses/30/lessons/67257
def operate(processedExp, oper_rank):
    while len(processedExp) > 1:
        oper_start = [-1] * len(oper_rank)

        # 각 연산이 시작하는 인덱스 확인
        for i in range(1, len(processedExp), 2):
            for j in range(len(oper_rank)):
                if processedExp[i] == oper_rank[j] and oper_start[j] == -1: 
                    oper_start[j] = i

        # 연산 작업 수행
        for j in range(len(oper_start)):
            if oper_start[j] != -1: 
                left_num = processedExp[oper_start[j] - 1]
                right_num = processedExp[oper_start[j] + 1]
                if oper_rank[j] == '*':
                    result_num = left_num * right_num
                elif oper_rank[j] == '+':
                    result_num = left_num + right_num
                elif oper_rank[j] == '-':
                    result_num = left_num - right_num

                processedExp.pop(oper_start[j] - 1)
                processedExp.pop(oper_start[j] - 1)
                processedExp[oper_start[j] - 1] = result_num
                break
                
    return processedExp[-1]



def solution(expression):
    from itertools import permutations
    import copy
    """
    2100-2152
    goal: 우선순위에 따라 연산을 구현하자
    * 우선순위는 완전탐색
    """
    answer = 0
    operations = ['+', '-', '*']
    
    # 1. 연산을 위한 입력값 전처리
    processedExp = ['']
    for char in expression:
        if char.isdigit():
            processedExp[-1] += char
        else:
            processedExp[-1] = int(processedExp[-1])
            processedExp.append(char)
            processedExp.append('')
    processedExp[-1] = int(processedExp[-1])
    
    
    # 2. 연산 우선순위 완전 탐색 
    for oper_rank in permutations(operations, 3):
        oper_result = operate(copy.deepcopy(processedExp), oper_rank)
        answer = max(abs(oper_result), answer)
    
    return answer
