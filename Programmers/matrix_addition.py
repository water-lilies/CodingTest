# 행렬의 덧셈
'''
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
'''

def solution(arr1, arr2):
    answer = []
    row_list = [] # answer에 append해줄 row 임시저장
    for i in range(len(arr1)): 
        for j in range(len(arr1[i])):
            row_list.append(arr1[i][j] + arr2[i][j])
        answer.append(row_list)
        row_list = []
    return answer


# 다른사람 풀이
import numpy as np 
def sumMatrix(A,B):
    A = np.array(A)
    B = np.array(B)
    answer = A+B
    return answer.tolist()

# zip이용
# zip은 동일한 개수로 이뤄진 iterable 한 자료형을 튜플로 묶어준다 
# ex) list(zip([1,2,3], [4,5,6])) -> [(1,4),(2,5),(3,6)]
def solution(arr1, arr2):
    return [[c+d for c, d in zip(a,b)] for a, b in zip(arr1,arr2)]

# 중첩 for문을 list comprehension에 넣기
def sumMatrix(A,B): 
    answer = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))] 
    return answer
