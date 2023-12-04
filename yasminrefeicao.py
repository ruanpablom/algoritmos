ref = []
for i in range (3):
  ref.append(int(input()))

ped = []
for i in range (3):
  ped.append(int(input()))

# CERTO
def refeicao(ref, ped):
  total = 0
  for i in range (3):
    sem = ref[i] - ped[i]
    if sem >= 0:
      total += 0
    else:
      sem < 0
      total += sem
  return abs(total)

resultado = refeicao(ref, ped)
print(resultado)