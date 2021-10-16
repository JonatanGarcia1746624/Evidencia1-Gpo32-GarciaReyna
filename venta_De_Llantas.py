#MODULOS QUE SE UTILIZARAN
from collections import namedtuple
import datetime
import time

#FUNCIONES A UTILIZAR
#1.CONTAR ELEMENTOS EN LA LISTA
def contar_ElementosEnLaLista(lista):
    numElementos = len(lista)
    return numElementos


#LISTA DONDE SE REGISTRAN LAS VENTAS
ventas_List = {}

#SWITCH PARA SALIR DEL WHILE
Salida = int(0)
while Salida == int(0):
    #FORMATO DE LA LISTA DE VENTAS
    venta_Info = namedtuple("VENTA","infoVenta")

    #REGISTRO DE ARTICULOS VENDIOS
    articulos_Vendidos = namedtuple("ARTICULOS","DatosArticulo,Precio")
    #MENU
    print(f'LLANTAS EL "TÍO JUAN"')
    print(f'1.REGISTRAR UNA VENTA')
    print(f'2.CONSULTAR UNA VENTA')
    print(f'3.SALIR\n')

    #OPCIÓN DEL USUARIO
    print(f'SELECCIONE EL NUMERO CORRESPONDINTE DE LA ACCIÓN A REALIZAR')
    op = input("OPCIÓN: ")

    if op == '1':
        elementos_ActualesEnLista = contar_ElementosEnLaLista(ventas_List)
        folio = elementos_ActualesEnLista + 1
        print("PORFAVOR INGRESE LOS ARTICULOS QUE SE VENDIERON")