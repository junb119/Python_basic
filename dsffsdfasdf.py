a, b = map(float, input().split())

if a < 150:
    weight = a - 100
elif a >= 160:
    weight = (a-100)*0.9
else:
    weight = (a - 150) / 2 + 50
    
bmi = (b -weight) * 100 / weight

if bmi <= 10:
    print('정상')
elif bmi > 20 :
    print('비만')
else:
    print('과체중')