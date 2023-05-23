def convert(time):
    # 분으로 변환
    h, m = time.split(':')
    h = int(h)
    m = int(m)
    return (h * 60) + m

def solution(book_time):
    """
    22:28
    22:46 첫번째 시도 실패
    23:02 room 배열을 계속 추가할 필요없이 하나의 배열로 해결 가능한 문제였음!
    
    1. 분으로 변환
    2. room 배열 선언
    3. book_time을 돌리면서
    - room 배열에 해당 시간 범위 + 1
    4. 정답은 room 배열중에서 가장 높은 값을 반환
    """
    room = [0] * (convert('23:59') + 10)
    # print(len(room[0]))
    
    for start, end in book_time:
        start = convert(start)
        end = convert(end) + 10 # 청소시간 추가
        
        # 기존방에서 사용가능한 방이 있는지 확인
        for i in range(start, end):
            room[i] += 1

    answer = max(room)
    return answer
