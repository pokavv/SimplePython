a = 1
b = 1

while a < 10:
  b = 1
  while b < 10:
      val = a * b
      print("{} * {} = {}".format(a, b, val))
      b += 1
  a += 1