k = int(input())

fibo_ant = 0
fibo_atual = 1
resultado = 0
while k > 0:
  for i in range(fibo_ant+1, fibo_atual):
    resultado = i
    k-=1
    if(k == 0): 
      break
  aux = fibo_ant + fibo_atual
  fibo_ant = fibo_atual
  fibo_atual = aux
  
print(resultado)