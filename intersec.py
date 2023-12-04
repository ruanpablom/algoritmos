vetor1 = []
vetor2 = []

tam = 15

for i in range(tam):
  vetor1.append(int(input()))

for j in range(tam):
  vetor2.append(int(input()))

for k in range(tam):
  for l in range(tam):
    if vetor1[k] == vetor2[l]:
      print(vetor1[k])
