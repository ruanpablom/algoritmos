entrada = round(float(input()), 2)

notasValidas = [100, 50, 20, 10, 5, 2]
qtdDeNotas = [0, 0, 0, 0, 0, 0]
moedasValidas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
qtdDeMoedas = [0, 0, 0, 0, 0, 0]

while entrada > 0:
  if entrada >= 2:
    for i in range(len(notasValidas)):
      if entrada >= notasValidas[i]:
        entrada -= notasValidas[i]
        entrada = round(entrada, 2)
        qtdDeNotas[i] += 1
        break
  else:
    for i in range(len(moedasValidas)):
      if entrada >= moedasValidas[i]:
        entrada -= moedasValidas[i]
        entrada = round(entrada, 2)
        qtdDeMoedas[i] += 1
        break
  

print('NOTAS:')
for i in range(len(qtdDeNotas)):
  print(f'{qtdDeNotas[i]} nota(s) de R$ {notasValidas[i]:.2f}')
print('MOEDAS:')
for i in range(len(qtdDeMoedas)):
  print(f'{qtdDeMoedas[i]} moeda(s) de R$ {moedasValidas[i]:.2f}')