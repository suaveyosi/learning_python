def sublist(lst1, lst2):
  pos_before=-2
  pos_sig=0
  for i in range(len(lst2)-1):
    if lst2[i] in lst1 and lst2[i+1] in lst1:
      pos_before = lst1.index(lst2[i])
      print(lst1)
      lst1.remove(lst2[i])
      print(lst1)
      pos_sig=lst1.index(lst2[i+1])
      print("pos_before {}, pos_sig {}".format(pos_before,pos_sig))
    if pos_before+1 == pos_sig:
      continue
    else:
      return 0
  return 1
    

A=[1,2,3,3,4]
B=[3,3]
print(sublist(A,B))
