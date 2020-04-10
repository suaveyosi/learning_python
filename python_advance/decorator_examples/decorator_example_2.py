# Usamos el decorador hijoputa para añadir hijoputa a cada frase
def hijoputa(f):
    def add_hijoputa(*args,**kwargs):
        x = f(*args,**kwargs)
        return "hijoputa "+x
    # Recordar devolver una función
    return add_hijoputa

@hijoputa
def recogiste():
    return "has recogido?"

@hijoputa
def limpiaste():
    return "has limpiado?"

print(recogiste())
print(limpiaste())