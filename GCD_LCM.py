# 최대공약수 최소공배수
'''
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 
solution(3, 12)는 [3, 12]를 반환해야 합니다.
'''



def solution(n, m):

    multi = n*m
    if n < m :
        n,m = m,n   # m이 작은 값이 되도록
    while m !=0:
        (n,m) = (m , n%m)
    return [n, multi//n]


# 유클리드 호제법 
'''
큰 숫자를 작은 숫자로 나누어 나머지를 구함으로써 최대공약수를 구하는 방법
나머지가 0이 될 때 작은 숫자가 최대공약수가 된다.
'''


# 다른사람 풀이

from fractions import gcd
def gcdlcm(a, b):
    return [gcd(a,b), a*b/gcd(a,b)]


from math import gcd
def solution(n,m):
    answer = []

    answer.append(gcd(n,m))
    answer.append(n*m//gcd(n,m))
    return answer 