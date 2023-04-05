# 하샤드 수
def solution(x):
    str_x = str(x)
    answer = 0
    for i in str_x:
        answer += int(i)
    return x % answer == 0
  
# other code
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0
