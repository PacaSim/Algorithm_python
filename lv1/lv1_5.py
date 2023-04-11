# 음양 더하기
def solution(absolutes, signs):
    answer = []
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer.append(absolutes[i])
        else:
            answer.append(-absolutes[i])          
    return sum(answer)

# 다른사람 코드
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# 제일 작은 수 제거하기
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        
        return arr
    else:
        return [-1]
    
# 없는 숫자 더하기
def solution(numbers): 
    return sum(range(10)) - sum(numbers)

# 가운데 글자 가져오기
def solution(s):
    length = len(s)
    quotient = length // 2
    if length % 2 == 0:
        return s[quotient - 1] + s[quotient]
    else:
        return s[quotient]
    
# 최적 코드
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]

# 수박수박수박수박수박수?
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer
