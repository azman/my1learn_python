# howto: loops (iteration)

loop = 0
while loop < 100:
  loop = loop + 1
  if loop==9:
    break
  elif loop==4:
    continue
  print(loop)

print("-- Range:")
for loop in range(3):
  print(loop)

print("-- Spell:")
for that in "pisang goreng":
  if that==' ':
    continue
  print(that)
