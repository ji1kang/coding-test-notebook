def solution(plans):
    """
    2335-0009
    """
    
    # 1. 과제 시간 별로 정렬 큐로 생성 + 분단위로 변환 (계산 편리)
    
    num_plans = len(plans)
    
    for i, (name, start, time) in enumerate(plans):
        hh, mm = start.split(':')
        start = int(hh) * 60 + int(mm)
        plans[i] = [name, start, int(time)]
        
    plans.sort(key=lambda x: x[1])
    
    # 2. 과제 진행
    todo = []
    done = []
    
    for i in range(num_plans-1): # 다음 과제랑 비교해야해서
        name, start, time = plans[i]
        next_start = plans[i+1][1]
        remain_time = next_start - time - start
        
        
        if remain_time > 0: # 시간이 남았을 때
            done.append(name)
            
            # 여러개가 있을 수 있으므로 반복을 돌려야 함
            while todo:
                recent_name, recent_time = todo.pop()
                remain_time -= recent_time
                
                if remain_time < 0:
                    todo.append([recent_name, remain_time * (-1)])
                    break
                else:
                    done.append(recent_name)
            
        elif remain_time < 0: # 못할 때 -> todo에 넣기
            todo.append([name, remain_time * (-1)])
        
        else: # 남은 시간이 0일 때 -> 바로 다음 진행
            done.append(name)
            continue 
        
    
    
    # 남은 과제 처리
    done.append(plans[-1][0])
    done.extend([name for name, _ in todo[::-1]])
    
    return done
