# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    """
    2100 - 2159
    
    """
    
    index = 0
    state = [None] * (n + 1)
    for depth in range(1, n + 1):
        state[depth] = [index, index + depth - 1]
        index += depth
    
    count = 0
    command = 'down'
    depth = 1
    last_depth = n
        
    num_answer = sum(range(n+1))
    answer = [None] * (num_answer)
    
    while count < num_answer:
        if command == 'down':
            answer[ state[depth][0] ] = count + 1
            state[depth][0] += 1
            if depth == last_depth:
                command = 'right'
            else:
                depth += 1
        elif command == 'right':
            answer[ state[depth][0] ] = count + 1
            state[depth][0] += 1
            if state[depth][0] > state[depth][1]:
                command = 'up'
                depth -= 1
                last_depth -= 1
        else:
            answer[ state[depth][1] ] = count + 1
            state[depth][1] -= 1
            if state[depth][0] > state[depth][1]:
                command = 'down'
                depth += 1
            else:
                depth -= 1
                
                
        count += 1
    
    return answer
