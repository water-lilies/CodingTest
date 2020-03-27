# 문자열 내림차순으로 배치하기
'''
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

제한 사항
str은 길이 1 이상인 문자열입니다.
'''

def solution(s):
    return ''.join(sorted(s, reverse=True))


# sort와 sorted의 차이
# list.sort() --> 원본을 직접 정렬. None을 반환
# sorted(list) -->  원본에 영향을 끼치지 않음. 새로운 list반환


# 다른사람 풀이

def solution(s):
    ls = list(s)
    ls.sort(reverse = True)
    return "".join(ls)