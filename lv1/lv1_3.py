# 1. 하샤드 수
def solution(x):
    str_x = str(x)
    answer = 0
    for i in str_x:
        answer += int(i)
    return x % answer == 0
  
# other code
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0

# 2. 두 정수 사이의 합
def solution(a, b):
    if a > b:
        return sum(list(range(b, a+1)))
    else:
        return sum(list(range(a, b+1)))
