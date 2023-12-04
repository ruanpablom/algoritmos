hora_incial = int(input())
minuto_inicial = int(input())
hora_final = int(input())
minuto_final = int(input())

inicio = hora_incial * 60 + minuto_inicial
final = hora_final * 60 + minuto_final

duracao = final - inicio

if duracao <= 0:
    duracao += 24 * 60

duracao_horas = duracao // 60
duracao_minutos = duracao % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao_horas, duracao_minutos))