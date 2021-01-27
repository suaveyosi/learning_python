def upperElement(A):
  '''return the highest element in a given list '''
  A.sort()
  return A[-1]

B=[1,4,2]
C=[-3,4,-8]
print(upperElement(C))