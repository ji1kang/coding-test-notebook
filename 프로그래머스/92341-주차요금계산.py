# https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math

def calc_price(mm, fees):
    basetime, baseprice, addtime, addprice = fees
    
    price = baseprice
    if mm > basetime:
        exceedtime = math.ceil((mm - basetime) / addtime) 
        price += (exceedtime * addprice)
        
    return price
    

def convert_time(hhmm):
    hh, mm = hhmm.split(':')
    return 60 * int(hh) + int(mm)
    

def solution(fees, records):
    from collections import defaultdict
    answer = []
    db = defaultdict(list)
    
    # 1. 차량번호 별로 입차시간, 출차시간 저장해두기
    for r in records:
        hhmm, car, _ = r.split(' ')
        db[car].append(hhmm)
    
    # 2. 누적 시간 계산
    # - 저장된 스케쥴을 2개씩 빼면 됨
    # - 저장된 배열이 홀수 일경우 '23:59' 추가
    for car in db:
        cumtime = 0
        if len(db[car]) % 2 != 0:
            db[car].append('23:59')
        
        for i in range(0, len(db[car]), 2):
            end = convert_time(db[car][i+1])
            start = convert_time(db[car][i])
            
            cumtime += (end - start)
            
        answer.append([car, calc_price(cumtime, fees)])
    
    
    
    return [price for _, price in sorted(answer, key= lambda x: x[0])]
