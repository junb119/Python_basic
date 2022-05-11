'''
https://programmers.co.kr/learn/courses/30/lessons/64061/solution_groups?language=python3&type=all 
참조
'''
def solution(board, moves):
    
    bucket = []
    cnt = 0
    for crane in moves :

        for line in range(len(board)):

            if  board[line][crane-1] == 0:
                continue
            else:
                bucket.append(board[line][crane-1]) 
                board[line][crane-1] = 0

                if len(bucket) <= 1:
                    break

                elif bucket[-1] == bucket[-2]:
                    bucket.pop(-1)
                    bucket.pop(-1)
                    cnt += 2
                break
    return cnt


'''
ver2
def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a

ver3
def solution(p,n):
    b=[];a=0
    for m in n:
        d=0;m-=1
        for i in range(0,len(p)):
            if(0!=p[i][m]):d=p[i][m];p[i][m]=0;break
        if(0==d):pass
        elif(0==len(b)):b.append(d)
        elif(d==b[-1]):b.pop();a+=2
        else:b.append(d)
    return a



'''