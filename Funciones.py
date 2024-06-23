#Funciones Biblioteca
import time,os,msvcrt
import json

libreria=[]
def opc1():
    print('Añadir libro: ')
    titulo=input('Ingresa el titulo de el libro: ')
    anio_publicacion=int(input('Ingrese el año de publicación: '))
    gen_libro=input('Ingrese genero de el libro: ')
    libros={'nombre':titulo,
            'año':anio_publicacion,
            'genero':gen_libro}}
    libreria.append(libros)
    time.sleep(2)
    print('LIBRO AGREGADO CON ÉXITO...')
def opc2():
    pass
def opc3():
    pass
def opc4():
    pass
def opc5():
    pass
def Salir():
        print('Adiooos..')
        exit()