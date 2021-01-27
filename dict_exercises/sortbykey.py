def sortbykey(dc):
  print(dc)
  sorted(dc)
  keys=sorted(dc)
  result={k:dc[k] for k in keys}
  return result

A={'Italia':'Milan','España':'Madrid'}
print(sortbykey(A))