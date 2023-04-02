# 나머지가 1이 되는 수 찾기
def solution(n):
    for x in range(1, n):
        if n % x == 1:
            return x

# 문자열 내 p와 y의 개수
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
  
# 정수 제곱근 판별
def solution(n):
    for x in range(1, n+1):
        if x ** 2 == n:
            return (x+1) ** 2
    return -1
            
# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    str_n = str(n)
    for i in str_n:
        answer.insert(0, int(i))
    return answer
  
# 정수 내림차순으로 배치하기
def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))
