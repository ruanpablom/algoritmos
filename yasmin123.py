entrada = input()

possiveisValores = {'one':1, 'two':2, 'three':3}
tamanhoEntrada = len(entrada)

for i in possiveisValores.keys():
  tamanhoKey = len(i)
  if tamanhoKey != tamanhoEntrada:
    continue
  
  qtdErros = 0

  for j in range(tamanhoEntrada):
    if i[j] != entrada[j]:
      qtdErros += 1
    if qtdErros > 1:
      break
  
  if qtdErros == 1:
    print(possiveisValores[i])
    break