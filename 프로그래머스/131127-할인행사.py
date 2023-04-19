# https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    """ 23:00 - 23:33
    조건
    - 10^5일동안 1일 1할인
    - 할인제품은 하나만 구매
    
    입력값
    - 원하는 제품과 수량
    - 할인내용과 비교하여 다 맞는지 확인
    
    출력값
    - 원하는 제품을 모두할인 받을 수 있는 회원등록의 날짜의 총일수
    """
    answer = 0
    
    data = {w: i for i, w in enumerate(want)}
    # 초기화
    day10 = [0] * len(want)
    for item in discount[:10]:
        if item in data:
            day10[data[item]] += 1
    
    n = len(discount)
    for i in range(n):
        if i+10 < n:
            # 현재에서 조건을 충족하는지 확인
            # print(i, day10, number, discount[i], discount[i+9], discount[i+10])
            if day10 == number:
                answer +=1 # 맞을 경우 더해줌

            # 다음걸로 업데이트
            if discount[i+10] in data:
                day10[ data[discount[i+10]] ] += 1

            # 이전건 지우기
            if discount[i] in data:
                day10[ data[discount[i]] ] -= 1
            
    if day10 == number:
        answer +=1
        
    # print(day10)
    
    
    return answer
