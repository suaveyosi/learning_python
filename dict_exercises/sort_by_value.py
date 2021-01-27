def sort_by_value(A):
  ''' Devuelve diccionario ordenado por el valor de mayor a menor'''
  values=sorted(list(A.values()),reverse=True)
  result={}
  for v in values:
    result[return_key(v,A)]=v
  print(result)

def return_key(v,A):
  for key,value in A.items():
    if v==value:
      return key

A={'Math':81, 'Physics':83, 'Chemistry':87}
sort_by_value(A)