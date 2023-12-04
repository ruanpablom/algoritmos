n = int(input())
for _ in range (n):
  en = input().split(' ')
  x = int(en[0])
  y = int(en[1])
  soma = 0
  for i in range (x, y):
    if i % 2 != 0:
      soma += i
  print(soma)