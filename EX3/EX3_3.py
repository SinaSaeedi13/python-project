def EX3_3(news):
  t = 0
  y = 0
  for direction in news:
    if direction == "n":
      t += 1
    elif direction == "e":
      y += 1
    elif direction == "s":
      t -= 1
    elif direction == "w":
      i -= 1
  if y == 3 and t == 2:
    return True
  elif y == -4 and t == 3:
    return True
  else:
    return False
