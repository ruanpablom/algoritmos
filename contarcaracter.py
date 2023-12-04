def contarCaracteres(entrada):
  entrada = entrada.split(' ')

  retorno = []

  for i in entrada:
    retorno.append(len(i))

  return retorno

print(contarCaracteres('UDESC'))