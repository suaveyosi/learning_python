import yaml
from prettytable import PrettyTable

def parse_info(file_to_open):
    with open(file_to_open) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    # En data tenemos una lista de diccionarios, cada elemento de la lista es una tarea de Ansible
    return data


def find_different_tags(data):
    "Funcion para encontrar las diferentes tags en todo el documento"
    tags = []
    for a in range(len(data)):
        compare_tags = data[a]['tags']
        for tag in compare_tags:
            if tag not in tags:
                tags.append(tag)

    return tags


def dict_name_and_paths(data,tag,result):
    """ Funcion que crea un diccionario con el nombre del tag, el nombre de los diccionarios que se crean para ese tag en ansible
        y los path que contiene cada diccionario """
    md = result.copy()
    tag_dict = {}
    # aux_dict es nombre del diccionario jboss_common_config y sus paths
    aux_dict = {}
    for a in range(0,len(data),3):
        # Tenemos que buscar que data[a] tenga paths, por que la tarea de Ansible es
        # find:
        #   paths:
        #     - "{{ role_path }}/vars/common/applications/nginx"
        # La siguiente tarea es el assert y la de después ya crea el diccionario. Por eso jugamos con a, a+1 y a+2
        # si es así vamos de 3 en 3, si no lo tiene saltamos 1. Actualizamos "manualmente"
        # lo que vale a
        while a<=len(data)-3 and 'find' not in data[a].keys():
            a += 1
        if a<= len(data)-3:
            if tag in data[a]['tags'] and tag in data[a+1]['tags'] and tag in data[a+2]['tags']:
                dict_name = data[a+2]['include_vars']['name']
                # Puede llamarse find paths o find path
                if 'path' in data[a]['find'].keys():
                    paths = data[a]['find']['path']
                elif 'paths' in data[a]['find'].keys():
                    paths = data[a]['find']['paths']

                aux_dict[dict_name] = paths
                tag_dict[tag] = aux_dict
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
    # Obtenemos el listado de tags diferentes
    diferent_tags = find_different_tags(data)
    result = {}
    for tag in diferent_tags:
        result = dict_name_and_paths(data,tag,result)
    print_table(result)
    # Las tareas van de 3 en 3, primero paths, luego assert y luego diccionario

if __name__ == "__main__":
    __main__()