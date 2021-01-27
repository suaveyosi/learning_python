def count_str(A):
  result=0
  for element in A:
    if len(element) >= 2:
      if element[0] == element [-1]:
        result+=1
  return result

A=['abcd','aba','1221']
print(count_str(A))

B=[1]
if not B:
  print("lista vacia")