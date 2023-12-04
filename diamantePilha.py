entrada = list(input().replace('.', ''))

pilha = []

qtdDiamantes = 0

for i in entrada:
  pilha.append(i)
  if len(pilha) > 1:
    if pilha[-1] == '>' and pilha[-2] == '<':
      qtdDiamantes += 1
      pilha.pop()
      pilha.pop()

print(qtdDiamantes)