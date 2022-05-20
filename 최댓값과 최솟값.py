'''
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 
이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

입출력 예
s	            return
"1 2 3 4"	    "1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	        "-1 -1"
'''
def solution(s):
    lst = list(map(int, s.split()))
    return "{0} {1}".format(min(lst), max(lst))

'''
ver2
def solution(s):
    s_list=s.split(" ")
    n = [int(i) for i in s_list]
    n.sort()

    return str(n[0]) + " " + str(n[len(n)-1])

ver3
def solution(s):
    il = sorted([int(c) for c in s.split(' ')])
    answer = ' '.join([str(il[0]), str(il[len(il)-1])])
    return answer

ver4
def solution(s):
    t = []
    if s[0] != "-":
        s = "+" + s
    for i in range(0, len(s)):
        t += [s[i]]
    for i in range(0, len(t)):
        if t[i] == " " and t[i+1] != "-":
            t.insert(i+1, "+")
    for i in range(1, len(t)):
        if t[len(t)-i] == " " and t[len(t)+1-i] != "-":
            t.insert(len(t)+1-i, "+")
            break
    print(t)
    result = []
    midcount1 = ""
    midcount2 = ""
    for i in range(len(t)):

        if t[i] == "-": 
            for j in range(i+1, len(t)):
                if t[j] != " ":
                    midcount1 = midcount1 + t[j]
                    if j == len(t)-1:
                        result += [-int(midcount1)]
                        midcount1 = ""
                        break
                elif t[j] == " ":
                    print(midcount1)
                    result += [-int(midcount1)]
                    midcount1 = ""
                    break

        elif t[i] == "+":
            for j in range(i+1, len(t)):
                if t[j] != " ":
                    midcount2 = midcount2 + t[j]
                    if j == len(t)-1:
                        result += [int(midcount2)]
                        midcount2 = ""
                        break
                elif t[j] == " ":
                    print(midcount2)
                    result += [int(midcount2)]
                    midcount2 = ""
                    break


    print(result)
    resultmax = int(result[0])
    resultmin = int(result[0])
    for i in range(len(result)):
        if resultmax < result[i]:
            resultmax = result[i]
    for i in range(len(result)):
        if resultmin > result[i]:
            resultmin = result[i]
    return "%s %s" % (resultmin, resultmax)


'''