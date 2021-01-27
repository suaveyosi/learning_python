def concat(a):
  b=""
  for el in a:
    b="".join(b,el)
  return b
A=['h','o','l','a']
print("".join(A))