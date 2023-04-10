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
