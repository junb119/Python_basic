'''
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
예를 들어 2와 7의 최소공배수는 14가 됩니다. 
정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

제한 사항
arr은 길이 1이상, 15이하인 배열입니다.
arr의 원소는 100 이하인 자연수입니다.

입출력 예
arr	        result
[2,6,8,14]	168
[1,2,3]	    6
'''
def solution(arr):
    arr.sort()
    mul = arr.pop()
    n = 1
    while True:
        answer = mul * n
        for i in range(len(arr)) :
            if answer % arr[i] == 0:
                if i == len(arr) -1 :
                    return answer
            else:
                n += 1
                break
'''
ver2
from fractions import gcd

def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def nlcm(num):
    num.sort()
    max_num = num[-1]
    # print (num, max_num)
    temp = 1
    for i in range(len(num)):
        # lcm = (a*b) / gcd
        # gcd = (a*b) / lcm
        temp = (num[i] * temp) / (gcd(num[i], temp))
        # print (temp)
    return temp

ver3

'''
