# https://school.programmers.co.kr/learn/courses/30/lessons/49993
def is_valid(skill_rule, skill_tree):
    skill_rule = [t for t in skill_rule]
    skill_tree = [t for t in skill_tree]
    
    # skill_rule이 비면 제약 없음 = 통과
    # skill_tree이 비면 체크 대상 없음 = 통과
    while skill_rule and skill_tree:
        # 선행스킬 대상 (skill_rule)일 경우 반드시 0번째 선행스킬과 0번째 스킬트리가 일치해야 함
        if skill_tree[0] in skill_rule:
            if skill_tree[0] == skill_rule[0]:
                skill_tree.pop(0)
                skill_rule.pop(0)
            else:
                return False
        else:
            skill_tree.pop(0)
    return True

def solution(skill, skill_trees):
    """
    2106 - 2117
    
    input: 스킬 우선순위 (중복 없음), 스킬트리 후보 (중복 없음)
    
    sol: 완전탐색 & 큐
    
    output: 스킬에 우선순위가 존재할 때
    가능한 스킬트리 순서 조합의 갯수
    """
    
    answer = 0
    for tree in skill_trees:
        if is_valid(skill, tree):
            answer += 1
    
    return answer
