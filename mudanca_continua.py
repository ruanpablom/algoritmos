from math import floor


m = float(input())

seconds_g = (6*60*60)/90

seconds_of_m = m * seconds_g + (6*60*60)

horario_hora = floor((seconds_of_m % (60 * 60 * 60)) / (60 * 60) % 24)
horario_min = floor((seconds_of_m % (60 * 60)) / ( 60))
horario_sec = floor((seconds_of_m % (60)))


if m < 90 or m == 360:
  print("Bom Dia!")
elif m < 180:
  print("Boa Tarde!")
elif m < 270:
  print("Boa Noite!")
elif m < 360:
  print("De Madrugada!!")

print('{:02d}:{:02d}:{:02d}'.format(horario_hora, horario_min, horario_sec))
