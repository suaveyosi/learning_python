def dict_from_list(A,B):
  '''Write a Python program to convert list to list of dictionaries. Go to the editor
  Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
  Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]'''

  result = { key:value for key in A for value in B}
  print(result)
A=["Black", "Red", "Maroon", "Yellow"]
B=["#000000", "#FF0000", "#800000", "#FFFF00"]
dict_from_list(A,B)