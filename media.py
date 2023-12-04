n_alunos = int(input())

media = 0

for i in range(n_alunos):
    nota = float(input())
    media = media + nota

media = media/n_alunos

print("%.1f" % media)