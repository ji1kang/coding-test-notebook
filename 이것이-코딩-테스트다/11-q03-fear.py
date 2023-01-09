# 2022-01-09 22:18 ~ 22: 46
# 그리디 문제 

# 조건
# 유저의 공포도 수치 >= 전체 유저의 수
# 모두를 넣을 필요는 없다

# 아웃풋
# 최대값 
# 1. 정렬 - 제일 큰애 한테 맞춰준다
# 2. 원소를 맞출 필요는 없다
# 3. (1-1) 제일 큰애 포함 큰애의 공포도 만큼 출력
# (1-2) 만약에 전체보다 큰애가 없으면 큰애를 아예 제외
# (2) 걔네 빼고 그 다음 큰애 포함 공포도 만큼 확인
# (3) 이 조건을 만나지 못하면 나간다

n = int(input())
users = list(map(int, input().split(' ')))
users.sort()
users.reverse()
    

num_groups = 0
while True:
    num_users = len(users)
    
    max_user = users[0]
    if max_user > num_users:
        # 조건 못맞춤
        max_user.pop(0)
    else:
        # 조건 맞추는 이용자 제외
        users = users[max_user:]
        num_groups += 1
        
    if num_users <= max_user:
        break
    
    
    

print(num_groups)

# output: possible group
