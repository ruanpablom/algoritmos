entrada = list(input().replace('.', ''))

qtdDiamantes = 0

comecoDeUmDiamanteIndex = -1
fimDeUmDiamanteIndex = -1

parada = False

while not parada:
  for i in range(len(entrada)):
    if entrada[i] == '<':
      comecoDeUmDiamanteIndex = i
    if entrada[i] == '>' and comecoDeUmDiamanteIndex != -1:
      fimDeUmDiamanteIndex = i
      entrada[comecoDeUmDiamanteIndex] = ' '
      entrada[fimDeUmDiamanteIndex] = ' '
      qtdDiamantes += 1
      comecoDeUmDiamanteIndex = -1
      fimDeUmDiamanteIndex = -1
      break
    if i == len(entrada) - 1:
      parada = True

print(qtdDiamantes) 