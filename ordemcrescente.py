vetor = []

tam = 30

for i in range(tam):
  vetor.append(int(input()))

vetor.sort()

for i in range(tam):
  print(vetor[i])