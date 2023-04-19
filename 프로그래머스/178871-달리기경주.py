# https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    
    player2idx = {name: i for i, name in enumerate(players)}
    
    for call_name in callings:
        call_index = player2idx[call_name]
        slow_index = call_index - 1
        slow_name = players[slow_index]
        
        
        players[call_index], players[slow_index] = players[slow_index], players[call_index]
        
        player2idx[slow_name] = call_index
        player2idx[call_name] = slow_index
        
    
    return players
