i = 0.0
while i <= 2:
  for j in range(1, 4):
    if i % 1 == 0:
      print("I={} J={}".format(int(i), int(j+i)))
    else:
      print("I={} J={}".format(i, j+i))
  i += 0.2
  i = round(i,1)

# I = 0
# J = 1

# while I <= 2:
#   for x in range(3):
#     if I % 1 == 0 or J % 1 == 0:
#         print(f"I={I:.0f} J={J:.0f}")
#     else:
#         print(f"I={I:.1f} J={J:.1f}")
#     J += 1
#   I += 0.2
#   J = I + 1