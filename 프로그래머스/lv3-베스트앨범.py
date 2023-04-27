# https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    """ 2235 - 2302 (히든테케2개 실패 - 3번 조건 생각 안해서 그런듯)
    sort key rank
    1. 누적 재생이 많은 장르 순
    2. 누적 재생이 많은 노래 순
    3. 고유 번호가 낮은 노래 순
    """
    import heapq as hq
    data = {} # 2,3번 조건을 위한 딕셔너리
    meta = {} # 1번 조건을 위한 딕셔너리
    
    # 데이터 필터링 
    idx = 0
    for g, p in zip(genres, plays):
        # 장르 재생 합산 계산
        if g not in meta:
            meta[g] = 0
        meta[g] += p
        
        # 장르별 Top2 재생 곡 확인 - 길어지면 나중에 정렬할 때 오래걸리니 힙큐 사용
        if g not in data:
            data[g] = [(p, idx)]
        else:
            if len(data[g]) == 1:
                data[g].append((p, idx))
                hq.heapify(data[g])
            elif len(data[g]) >= 2:
                if p > data[g][0][0]: # 가장 작은 수록곡 플레이 보다 재생횟수가 많으면 교체
                    data[g][0] = (p, idx)
                    hq.heapify(data[g])
        idx += 1
        
    
    # 출력 - 원래 조건의 반대로 구한 뒤 reverse 하도록 구현
    answer = []
    for key in sorted(meta, key = lambda key: meta[key]):
        if len(data[key]) == 2 and data[key][0][0] == data[key][1][0]: # 2개 모두 같을 조건 고려
                answer.append(data[key][1][1]) # 위에서 들어올 때 낮은 인덱스부터 들어오니까 뒤에 있는게 항상 높은 인덱스
                answer.append(data[key][0][1])
        else:
            answer.extend([idx for _, idx in data[key]])
        
    
    
    return answer[::-1]
