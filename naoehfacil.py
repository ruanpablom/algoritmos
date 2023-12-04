def eh_facil(sobrenome):
    consoantes_consecutivas = 0
    for letra in sobrenome:
        if letra.isalpha() and letra not in 'AEIOUaeiou':
            consoantes_consecutivas += 1
            if consoantes_consecutivas >= 3:
                return "nao eh facil"
        else:
            consoantes_consecutivas = 0
    return "eh facil"

casosDeTeste = int(input())

for i in range(casosDeTeste):
    sobrenome = input()
    print(f'{sobrenome} {eh_facil(sobrenome)}')