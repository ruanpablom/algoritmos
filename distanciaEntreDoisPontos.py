def distancia(coordenadasPonto1, coordenadasPonto2):
    x1, y1 = coordenadasPonto1
    x2, y2 = coordenadasPonto2
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 4)

print(distancia([2.5, -0.4], [-12.2, 7.0]))