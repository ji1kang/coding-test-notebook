# https://school.programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    """
    2106
    
    input: 스킬 우선순위 (중복 없음), 스킬트리 후보 (중복 없음)
    sol: 완전탐색
    output: 스킬에 우선순위가 존재할 때
    가능한 스킬트리 순서 조합의 갯수  
    """
    skill_rule = [t for t in skill]
    
    answer = 0
    for tree in skill_trees:
        ans = ''.join(filter(lambda x: x in skill_rule, tree))
        if ans == skill[:len(ans)]:
            answer += 1

    return answer
