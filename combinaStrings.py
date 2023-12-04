def combinaString(e1,e2):
  tamanhoe1 = len(e1)
  tamanhoe2 = len(e2)
  menorTamanho = tamanhoe1 if tamanhoe1 < tamanhoe2 else tamanhoe2
  stringCombinada = ''
  for i in range(menorTamanho):
    stringCombinada += e1[i]
    stringCombinada += e2[i]
  if tamanhoe1 > tamanhoe2:
    stringCombinada += e1[menorTamanho:]
  else:
    stringCombinada += e2[menorTamanho:]
  return stringCombinada

print(combinaString('TD_DS','ASUEC'))