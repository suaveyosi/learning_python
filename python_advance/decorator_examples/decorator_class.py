# We can make a class to count how many times a funcion is called
class Counter():
    def __init__(self,f):
        self.f = f
        self.counter = 0

    # La clase debe tener un __call__() que se va a usar cada vez que es llamada
    def __call__(self,*args,**kwargs):
        self.counter += 1
        # MUY IMPORTANTE: debemos devolver una función
        return self.f(*args,**kwargs)

@Counter
def hello(name):
    print("hola {}".format(name))

hello("Juan")
hello("jose")
hello("Pepito")
print(hello.counter)