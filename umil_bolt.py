t = int(input())
while t > 0:
  menor = 14.0
  for t_i in range(1, t+1):
    tentativa = float(input())
    if tentativa < menor:
      menor = tentativa
  print("%.2f" % menor)
  t = int(input())