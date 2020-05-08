# 약수의 합
'''
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.

'''

def solution(n):
    answer = 0

    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    
    return answer



# 다른사람 풀이 1
def sumDivisor(num): 
    return sum([i for i in range(1, num+1) if num % i == 0])


# 다른사람 풀이 2
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

