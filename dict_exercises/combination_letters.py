def combine(*multiple_list):
  '''function that extracts combinations of letters from multiple different lists'''
  inner_index=0
  outer_index=0
  result=[]
  listas=multiple_list[0]
  print(listas)
  letra_ant=''
  mystr=''
  while outer_index < len(listas):
    while inner_index < len(listas[outer_index]):
      print("dentro: inner_index {}".format(inner_index))
      print(listas[outer_index][inner_index])
      #print(listas[outer_index][inner_index]+listas[outer_index][inner_index+1])
      mystr=mystr+listas[outer_index][inner_index]
      print(mystr)
      inner_index=inner_index+1
    result.append(mystr)
    outer_index=outer_index+1
    inner_index=0
    mystr=''
  print(result)
def extract_from_dict(A):
  lists=list(A.values())

  combine(lists)

A={'1':['a','b'],'2':['c','d']}
lista=list(A.values())
B=[a+b for a in lista[0] for b in lista[0]]
print(B)
#extract_from_dict(A)