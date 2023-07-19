# https://school.programmers.co.kr/learn/courses/30/lessons/120956#
def solution(babbling):
    # 2050 - 2140
    answer = 0

    for word in babbling:
        speak = ["aya", "ye", "woo", "ma"]
        
        # 단어와 발음 가능한 단어가 모두 존재할 때 작업
        while word and speak:
            new_speak = []
            for s in speak:
                end = len(s)
                if not word:
                    break
                elif len(word) >= end and s[:end] == word[:end]:
                    word = word.replace(s, '', 1)
                else:
                    new_speak.append(s)
            
            # 표현할 수 없는 경우
            if len(speak) == len(new_speak):
                break
            
            speak = new_speak
            
        # 발음에 성공한 경우
        if word == '':
            answer += 1    

    return answer
