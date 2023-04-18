# https://school.programmers.co.kr/learn/courses/30/lessons/134240
def solution(food):
    from collections import OrderedDict
    """
    0020 - 0036
    
    - 매 대결 음식의 종류와 양이 바뀜
    - 한 선수는 왼쪽부터, 다른 선수는 오른쪽부터
    - 중앙에는 물이 있음
    
    - 두선수가 먹는 음식 종류와 양, 순서가 같아야 함
    - 단, 칼로리가 낮은 음식부터 먹어야 함
    
    - 입력값
    - [n번음식, 갯수, ...] 단, 0은 물
    
    - 출력값
    - 음식의 배치(최종)
    
    
    - Todo
    - {index: freq} 딕셔너리 생성하면서 짝수 인지 확인, 아닐 경우 - 1 + 음식의 총합을 센다
    - 배열 생성 (음식 총합 + 1)
    - 왼쪽만 구하면 오른쪽은 자동적으로 구해지므로 range(0, mid) 까지 돌면서
    - 왼쪽부터 배치   
    """
    answer = ''
    data = OrderedDict()
    cumsum = 0
    for i in range(1, len(food)):
        data[i] = food[i] if food[i] % 2 == 0 else food[i] -1
        cumsum += data[i]
    
    
    n = cumsum + 1
    mid = n // 2
    for i in data:
        answer += str(i) * (data[i] // 2)
        
    answer = answer + '0' + answer[::-1]
     
    
    return answer
