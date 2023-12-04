n = int(input())

fibo_ant = 0
fibo_atual = 1

for i in range(n):
  print(fibo_ant, end=" ")

  aux = fibo_ant + fibo_atual
  fibo_ant = fibo_atual
  fibo_atual = aux