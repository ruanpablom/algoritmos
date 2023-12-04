matriz = [[i*j for j in range(4)] for i in range(5)]

valores = []

for i in range(12):
  valores.append(int(input()))

for i in range(0, 12, 4):
  aux = matriz[valores[i]][valores[i+1]]
  matriz[valores[i]][valores[i+1]] = matriz[valores[i+2]][valores[i+3]]
  matriz[valores[i+2]][valores[i+3]] = aux

print(matriz)