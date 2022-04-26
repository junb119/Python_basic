'''
수박수박수박수박수박수?
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.
입출력 예
n	return
3	"수박수"
4	"수박수박"
'''

2
3
4
5
6
7
8
9
def solution(n):
    a = ''
    for i in range(n) :
        if i % 2 == 0 :
            a += '수'
        else:
            a += '박'
    return a

'''
ver2.

def water_melon(n):
    s = "수박" * n
    return s[:n]
    
ver3
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)


'''
