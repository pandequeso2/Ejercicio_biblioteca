#Ejercicio Biblioteca:
import os,time,msvcrt
import json
from Funciones import *

while True:
    print('Biblioteca\n1: Agregar un libro\n2: Mostrar libros\3: Buscar libros por titulo\n4:Modificar la información de un libro\n5: Imprimir en Json\n6: Salir.')
    opc=int('Ingrese una opcion: ')
    if opc==1:
        opc1()
    elif opc==2:
        opc2()
    elif opc==3:
        opc3()
    elif opc==4:
        opc4()
    elif opc==5:
        opc5()
    else:
        Salir()