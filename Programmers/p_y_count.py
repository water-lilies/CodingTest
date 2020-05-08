# 문자열 내 p와 y의 개수
'''
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 pPoooyY면 true를 return하고 
Pyy라면 false를 return합니다.
'''

def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False



# 다른사람 풀이 1
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')


# 다른사람 풀이 2
from collections import Counter
def numPY(s):
    c = Counter(s.lower())
    return c['y'] == c['p'] 