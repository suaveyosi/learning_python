def add_3(f):
    def suma_3(*args,**kwargs):
        x = f(*args,**kwargs)
        return 3+x
    return suma_3

@add_3
def suma(a,b):
    return a+b

print(suma(1,2))