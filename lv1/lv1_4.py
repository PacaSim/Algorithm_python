# 콜라츠추측
def solution(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        answer += 1
    if answer > 500:
        return -1
    else:
        return answer
        
# 서울에서 김서방 찾기
def solution(seoul):
    pos = seoul.index('Kim')
    return '김서방은 ' + str(pos) + '에 있다'

#나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer

# 다른 사람 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
