todasAsLetrasMaiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decifrar(texto_cifrado, chave):
  for i in range(len(texto_cifrado)):
    texto_decodificado = ''

    for j in range(len(texto_cifrado)):
      index = todasAsLetrasMaiusculas.find(texto_cifrado[j])
      index = index - chave
      index = index % 26
      texto_decodificado += todasAsLetrasMaiusculas[index]

  return texto_decodificado

texto_cifrado = input()
chave = int(input())

print(decifrar(texto_cifrado, chave))