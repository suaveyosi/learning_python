def to_ascii(f):
    def wrap(*args,**kwargs):
        x = f(*args,**kwargs)
        return ascii(x)
    return wrap


# Al ponerle el decorator to_ascii lo que hace es invocarme a mi función pasándole como parámetro northen_city
# Mi función to_ascii lo que hace es sustituir el caracter ø por su codificación ascii
@to_ascii
def northen_city():
    return "Tromsø"

print(northen_city())
#Esto me imprime 'Troms\xf8' si le quito el @to_ascii me imprime Tromsø