# This file is used to create an installable package from our code
# To execute it:
# python3 setup.py sdist
# This will create a dist directory with the python installable paquetecalculos-1.0.tar.gz
# The package contains all the .py files located under folder calculos_numericos/basicos
from setuptools import setup 
setup( 
        name="paquetecalculos", 
        version="1.0", 
        description="Paquete con funciones matematicas basicas", 
        author="David", 
        packages=["calculos_numericos","calculos_numericos.basicos"] 
) 