a,b = map(int, input().split())

if b % a == 0 :
  x = b // a
  print(f'{a}*{x}={b}')
elif a % b == 0 :
  x = a // b
  print(f'{b}*{x}={a}')
else:
  print('none')