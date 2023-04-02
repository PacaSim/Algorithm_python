# 짝수와 홀수
def solution(num):
    if num % 2 == 0:
        return "Even"
    else: return "Odd"
    
 # 평균 구하기
def solution(arr):
    return sum(arr) / len(arr)
  
# 약수의 합
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i) 
    return sum(answer)
  
# 자릿수 구하기
def solution(n):
    str_n = str(n)
    sum = 0
    for i in str_n:
        sum += int(i)
    return sum
  
# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer
