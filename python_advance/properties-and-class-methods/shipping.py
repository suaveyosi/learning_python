class ShippingContainer:
    # Class attribute
    next_serial = 1337

    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    # Alternativa a staticmethod, crear un classmethod
    @classmethod
    def _get_next_serial2(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # Naming constructor. Como puede ser usado por las clases hijas, lo complemento con el número indeterminado de parámetros
    @classmethod
    def empty_container(cls, owner_code, *args, **kwargs):
        return cls(owner_code,contents=None, *args, **kwargs)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # Para referenciar el atributo de clase tengo que usar el nombre de la clase
        self.serial = ShippingContainer._get_next_serial2()

# Clase hija que sólo admite crear un contenedor si no supera la máxima temperatura
class RefrigeratedShippingContainer(ShippingContainer):
    max_celsius = 4.0

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratedShippingContainer.max_celsius:
            raise ValueError("Temperature to hoot!")
        # Con _celsius indicamos que ese atributo es privado, no debería accederse desde fuera
        self._celsius = celsius

    # Mediante @property hacemos que un método pueda ser llamado como un atributo
    # Getter
    @property
    def celsius(self):
        return self._celsius

    # Setter. Mediante el decorator setter hacemos que valga para modificar
    @celsius.setter
    def celsius(self,value):
        if value > RefrigeratedShippingContainer.max_celsius:
            raise ValueError("Temperature to hoot!")
        self._celsius = value