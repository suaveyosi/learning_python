def concat_multiple(*args):
  ''' Function to concatenate multiple dictionaries passed as parameter '''
  result=[]
  mydic={}
  for element in args:
    if isinstance(element,dict):
      mydic.update(element)
    else:
      result.append(element)
  if result:
    print(result)
  else:
    print(mydic)

A={"España":"Madrid"}
B={"Italia":"Milán"}
concat_multiple("hola"," ","que", " ","tal")
concat_multiple(A,B)