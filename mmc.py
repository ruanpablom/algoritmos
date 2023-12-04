def mmc(x,y):
  if x > y:
    z = x
  else:
    z = y
  
  while(True):
    if((z % x == 0) and (z % y == 0)):
      result =z
      break
    z += 1
  return result

x=20
y=7

result = mmc(x,y)
print("Minimo Múltiplo Comum de:")
print("x=%d" % x)
print("y=%d" % y)
print("Resultado=%d" % result)