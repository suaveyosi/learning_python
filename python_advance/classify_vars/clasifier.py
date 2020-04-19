import yaml
from prettytable import PrettyTable

def parse_info(file_to_open):
    with open(file_to_open) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    # En data tenemos una lista de diccionarios, cada elemento de la lista es una tarea de Ansible
    return data


def find_different_tags(data):
    "Funcion para encontrar las diferentes tags en todo el "
    tags = []
    for a in range(len(data)):
        compare_tags = data[a]['tags']
        for tag in compare_tags:
            if tag not in tags:
                tags.append(tag)

    return tags


def get_names_of_tasks(data,tag):
    # Función que para cada tag nos devuelve el nombre de las tareas en las que aparece
    names = []
    md = {}
    for a in range(len(data)):
        if tag in data[a]['tags'] and 'name' in data[a].keys():
            names.append(data[a]['name'])
    md['names'] = names

    return md 

def find_paths(data,tag,dictionary):
    # Función que modifica el usa el diccionario que le pasa para crear uno nuevo en el que le añade los paths dentro del nombre 
    # de la tarea para cada tag
    # Buscaremos dentro de nombre si tiene path en data
    return_paths = dictionary.copy()
    md = {}
    names = dictionary[tag]['names']
    for num in range(len(data)):
        for n in names:
            
            if 'name' in data[num].keys():
                if n in data[num]['name'] and 'find' in data[num].keys():
                    print("dentro del if")
                    paths = data[num]['find']['path']
                    md['paths'] = paths
                    return_paths[tag].update(md)
    #md['paths'] = return_paths

def dict_name_and_paths(data,tag,result):
    md = result.copy()
    tag_dict = {}
    # aux_dict es nombre del diccionario jboss_common_config y sus paths
    aux_dict = {}
    for a in range(0,len(data),3):
        if tag in data[a]['tags'] and tag in data[a+1]['tags'] and tag in data[a+2]['tags']:
            print(data[a+2])
            print(tag)
            dict_name = data[a+2]['include_vars']['name']
            # Puede llamarse find paths o find path
            if 'path' in data[a]['find'].keys():
                paths = data[a]['find']['path']
            elif 'paths' in data[a]['find'].keys():
                paths = data[a]['find']['paths']

            aux_dict[dict_name] = paths
            tag_dict[tag] = aux_dict
            #tag_dict[tag].update(aux_dict)
    # Actualizamos el diccionario con cada nuevo
    md.update(tag_dict)
    return md

def print_table(data):
    x = PrettyTable()
    x.field_names = [ "TAG", "Diccionario", "Paths"]
    sub_dict = {}
    for key, subkey in data.items():
        for k1 in subkey.keys():
            x.add_row([key, k1, ""])
            for path in data[key][k1]:
                x.add_row(["","",path])

    print(x)

def __main__():
    # Primero parseamos toda la info del yaml
    data = parse_info("main.yml")
#    print(data[0])
#    print(data[1])
#    print(data[2])
    # Obtenemos el listado de tags diferentes
    diferent_tags = find_different_tags(data)
    result = {}
    for tag in diferent_tags:
        result = dict_name_and_paths(data,tag,result)
    #print(result)
    print_table(result)
    # Las tareas van de 3 en 3, primero paths, luego assert y luego diccionario

if __name__ == "__main__":
    __main__()