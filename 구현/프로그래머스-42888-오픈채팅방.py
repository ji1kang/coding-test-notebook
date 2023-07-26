# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    """
    2100 - 2121
    
    Goal: 닉네임 변경 작업 수행하기
    <조건>
    1. Change 요청이 들어왔을 때
    (1) 방 안에 없으면 방 안에 넣기
    (2) 방 안에 있으면 냅두기
    2. 기존 히스토리 업데이트 하기
    
    <비고>
    - 닉네임이 같을 수 있기 떄문에 uid로 관리 해야함
    """    
    from collections import defaultdict
    uid2nick = defaultdict(str)
    answer = []
    
    # 변경 작업
    for _input in record:
        _input = _input.split(' ')
        
        if len(_input) == 2:
            cmd, uid = _input
            answer.append((False, uid))
        else:
            cmd, uid, nick = _input
            if cmd == 'Enter':
                answer.append((True, uid))
                uid2nick[uid] = nick
            elif cmd == 'Change':
                uid2nick[uid] = nick
    
    
    return [f'{uid2nick[uid]}님이 들어왔습니다.' if state else f'{uid2nick[uid]}님이 나갔습니다.' for state, uid in answer]
