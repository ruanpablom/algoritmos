x = int(input())
y = int(input())

if x > 0 and y > 0:
  print("primeiro")
elif x < 0 and y > 0:
  print("segundo")
elif x < 0 and y < 0:
  print("terceiro")
elif x > 0 and y < 0:
  print("quarto")