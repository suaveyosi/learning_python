# Importanmos funciones para la generación de datos
import math 

""" A module to deal with bmp image files """
def write_grayscale(filename, pixels):
    """ Creates and writes a grayscale bmp file.
    Args:
        Filename: the name of the file
        pixels: A rectangular image stored as a squence of rows.
            Each row must be an iterable series of integers from 0-255
    Raises:
        ValueError: if any of the integers are out of range
        OSError: if the file couldn't be written
    """
    height = len(pixels)
    width = len(pixels[0])
    # Opening the file
    with open(filename, "wb") as bmp:
        # BMP header obligatorio para ficheros binarios
        bmp.write(b'BM')
        # En formato BMP, requiere a continuación 4 bytes indicando el tamaño del fichero. Como no lo sabemos todavía
        # almacenamos la posición en un puntero y ponemos dummy data (cuatro 0)
        size_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')

        # obligatorio 32 bits a 0
        bmp.write(b'\x00\x00')
        bmp.write(b'\x00\x00')

        # Otro puntero para almacenar el offset desde el principio del fichero hasta cuando empiezan los pixeles
        pixel_offset_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')

        # Cabecera de la imagen. Tenemos que escribir el tamaño de la cabecera de la imagen en 32 bits. 
        # En nuestro caso la cabecera son 40 bites (0x28). Al ser el binario formato little indian va de menos significativo
        # a mas significativo
        bmp.write(b'\x28\x00\x00\x00') # Image header size in bytes - 40 decimal
        # Ahora el tamaño en ancho y largo de la imagen. Usamos un método que nos devuelve justo lo que necesitamos. 
        # Le pasamos un numero y nos lo devuelve codificado a 32 bits
        bmp.write(_int32_to_bytes(width))
        bmp.write(_int32_to_bytes(height))
        # Bytes obligatorios que indican la escala de grises
        bmp.write(b'\x01\x00')
        bmp.write(b'\x08\x00')
        bmp.write(b'\x01\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')

        # Paleta de colores. Escala de grises
        for c in range(256):
            bmp.write(bytes((c, c, c, 0))) #Blue, Green, Red, Zero

        # Aquí ha terminado la cabecera y vienen los píxeles de nuestro rectángulo. Guardamos el puntero
        pixel_data_bookmark = bmp.tell()
        # Las imágenes bmp se escriben de abajo a arriba, así pues usamos reverse
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            # Los datos que vamos escribiendo tienen que ser múltiplos de 4 le añadimos un padding de 0 dependiendo los que necesite
            padding = b'\x00' * ((4 - len(row) % 4 ) % 4)
            bmp.write(padding)

        # End of file
        eof_bookmark = bmp.tell()

        # Ahora ya sabemos cuánto ocupa el fichero, vamos rellenando los huecos que dejamos con los datos correctos
        bmp.seek(size_bookmark) # Colocamos el puntero en el tamaño del fichero
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Pixel offset. Indicador de dónde empiezan los datos
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))

def _int32_to_bytes(i):
    """ Convert an Integer to four bytes indian format """
    # &: bitwise and. Comparador a nivel de bits
    # >>: right shift
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))

# Generador de datos
def mandel(real, imag):
    x = 0
    y = 0
    for i in range(1,257):
        if x*x + y*y > 4.0:
            break
        xt = real + x*x + y*y
        y = imag + 2.0 * x * y 
        x = xt
    return int(math.log(i) * 256 / math.log(256)) - 1

def mandelbrot(size_x, size_y):
    return [[mandel((3.5 * x / size_x) - 2.5,
                   (2.0 * y / size_y) - 1.0)
             for x in range(size_x)]
            for y in range(size_y)]

# Usando las funciones 
if __name__ == '__main__':
    pixels = mandelbrot(448,256)
    write_grayscale("rectangulo.bmp",pixels)


