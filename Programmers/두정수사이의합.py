'''
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

제한 조건
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.

'''

def solution(a, b):
    answer = 0
    if a > b :
        a,b = b,a
    for i in range(a, b+1):
        answer +=i
    return answer


# 다른사람 풀이

def adder(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2
    # 절대값 함수 사용

def adder(a, b):
    return sum(range(min(a,b),max(a,b)+1))
    # 최대최소값 사용