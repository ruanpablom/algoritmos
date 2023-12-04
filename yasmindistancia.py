def distancia(ponto1,ponto2):
  x1, y1 = ponto1
  x2, y2 = ponto2
  dis = (x2 - x1)**2 + (y2 - y1)**2
  raiz = dis**0.5
  return round(raiz, 4)

print(distancia([1,7],[5,9]))