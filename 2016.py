# 2016년
'''
2016년 1월 1일은 금요일입니다. 
2016년 a월 b일은 무슨 요일일까요? 
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다. 
예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.

제한 조건
2016년은 윤년입니다.
2016년 a월 b일은 실제로 있는 날입니다. 
(13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
'''

def solution(a, b):
    weeks = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    return weeks[(sum(days[:a-1])+b-1)%7]



# 다른사람 풀이
import datetime

def solution(a, b):
    day_of_the_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return day_of_the_week[datetime.datetime(2016, a, b).weekday()]

# daytime의 weekday는 해당 날의 요일을 숫자로 반환.
# weekday()함수는 0부터 6까지 월~일에 해당.