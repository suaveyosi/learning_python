from functools import reduce
def count_letter(doc):
    # Funcion que devuelve un diccionaro con el numero de palabras y las veces que aparecen
    # Pasamos a minusculas c es cada caracter
    normalized_doc = "".join(c.lower() if c.isalpha() else ' ' for c in doc)

    # Aquí creo un diccionario donde cada elemento es la letra en sí y el número de veces que aparece esa letra
    dictionary = { d:normalized_doc.count(d) for d in normalized_doc}

    return dictionary

def combine_d(d1,d2):
    d = d1.copy()
    for key, value in d2.items():
        # Tenemos que chequear si existe la clave en el primer diccionario, para evitar errores
        if key in d:
            d[key] = d[key]+ value
        else:
            d[key] = value
    return d

frases = ["IT Was the best of times. It was the worst of times", "Hola chaval, preparate para dejar de jugar"]
    
## En counts tengo el número de letras por separado para cada frase
counts = map(count_letter,frases)
## Ahora con combine y dreduce los junto
my_d = reduce(combine_d,counts)
print(my_d)