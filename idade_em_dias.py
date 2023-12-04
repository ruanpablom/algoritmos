n = int(input())

anos = n // 365
meses = (n - anos * 365) // 30
dias = n - (meses * 30) - (anos * 365)

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))