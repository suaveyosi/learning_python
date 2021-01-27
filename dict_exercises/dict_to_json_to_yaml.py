import json
import yaml
def dict_to_json(A,file_name):
  """
  docstring
  """
  with open(file_name, 'w') as jsonfile:
    json.dump(A,jsonfile)

A={'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
dict_to_json(A,"mydict.json")

def json_to_yaml(inputf,outputf):
  with open(inputf) as jsonfile:
    content=json.load(jsonfile)
    print(content)
  with open(outputf,'w') as yamlfile:
    yaml.dump(content,yamlfile)

json_to_yaml("mydict.json","mydict.yaml")