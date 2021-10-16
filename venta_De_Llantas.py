#MODULOS QUE SE UTILIZARAN
from collections import namedtuple
import datetime
import time

#LISTA DONDE SE REGISTRAN LAS VENTAS
ventas_List = {}

#SWITCH PARA SALIR DEL WHILE

Salida = int(0)
while Salida == int(0):
    #MENU
    print(f'LLANTAS EL "TÍO JUAN"')
    print(f'1.REGISTRAR UNA VENTA')
    print(f'2.CONSULTAR UNA VENTA')
    print(f'3.SALIR\n')

    #OPCIÓN DEL USUARIO
    print(f'SELECCIONE EL NUMERO CORRESPONDINTE DE LA ACCIÓN A REALIZAR')
    op = input("OPCIÓN: ")

    if op == '1':
        folio = int()
