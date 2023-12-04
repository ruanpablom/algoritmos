entrada = input().lower()
todasLetras = 'abcdefghijklmnopqrstuvwxyz'
qtdLetras = [0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0]

for i in range(len(entrada)):
  for j in range(len(todasLetras)):
    if entrada[i] == todasLetras[j]:
      qtdLetras[j] += 1

max_value = max(qtdLetras)

for i in range(len(qtdLetras)):
  if qtdLetras[i] == max_value:
    print(todasLetras[i], end='')