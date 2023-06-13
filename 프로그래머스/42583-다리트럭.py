# https://school.programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    
    """
    2203-2227
    
    3. 출력값: 모든 트럭이 다리를 건너는데 필요한 "최소값"
    
    2. 조건
    - 트럭의 최대 갯수
    - 트럭의 최대 하중 존재
    - 단, 다리에 완전히 올라야 무게로 친다
    - 순서대로 가야한다 = 트럭을 골라서 갈 필요 없음
    - t번째는 트럭 한대만 나올수 있고, 들어올때도 마찬가지
    
    1. 시간 복잡도
    - 10^4 = 딱히 무리 없음
    
    """
    t = 0 # time

    done = []
    
    doing = [0] * bridge_length
    num_truck = 0
    sum_weight = 0
    
    total_truck = len(truck_weights)
    
    while len(done) < total_truck:      
        # 매초 마다 차량 이동 필요
        done_truck = doing.pop(0)
        if done_truck != 0:
            done.append(done_truck)
            # 현재 트럭 갯수, 무게 갱신
            num_truck -= 1
            sum_weight -= done_truck
        
        if truck_weights and num_truck + 1 <= bridge_length and sum_weight + truck_weights[0] <= weight:
            # 트럭 갯수 초과 안하고 무게 초과 안할 때 = 추가 가능
            todo_truck = truck_weights.pop(0)
            doing.append(todo_truck) 
            num_truck += 1
            sum_weight += todo_truck
        else:
            doing.append(0) 
    
        
        t += 1
    
    
    return t
