h, w = map(int, input().split())

d=[]
val = 1
for i in range(h+1) :
    d.append([])
    for j in range(w+1) :
        # if i == 0 or j == 0 :
            d[i].append(0) 
        # else: 
            # d[i].append(val)
            # val += 1

n = int(input())
for i in range(n) :
    l, m, x, y = map(int,input().split())
    
    if m == 0 :
        for z in range(l) :
            d[x][y+z] = 1 
    else:
        for z in range(l):
            d[x+z][y] = 1
        
for i in range(1, h+1) :
    for j in range(1, w+1) : 
        print(d[i][j], end=' ')
    print()