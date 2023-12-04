count = 0

matriz = []

for i in range(5):
  matriz.append([])
  for j in range(5):
    matriz[i].append(count)
    count+=1

soma = 0

for i in range(5):
  soma = soma + sum(matriz[i])
  # for cols in matriz[i]:
  #   soma = soma + sum(cols)

media = soma / 25

print(soma)
print('{:.1f}'.format(media))