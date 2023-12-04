import re

numeroDeSenhas = int(input())

for i in range(numeroDeSenhas+1):
    senha = input()
    if (6 <= len(senha) <= 32 and
        re.search(r'[a-z]', senha) and
        re.search(r'[A-Z]', senha) and
        re.search(r'[0-9]', senha) and
        not re.search(r'\W', senha)):
        print('Senha valida.')
    else:
        print('Senha invalida.')