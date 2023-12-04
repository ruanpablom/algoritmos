l = int(input())
c = int(input())

matriz = []

for i in range(l):
  matriz.append([])
  for j in range(c):
    matriz[i].append(int(input()))

print(matriz)