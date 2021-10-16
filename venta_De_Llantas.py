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
    datos_Articulo = namedtuple("ARTICULOS","DescArticulo,Precio,fecha_venta")
    #MENU
    print(f'LLANTAS EL "TÍO JUAN"')
    print(f'1.REGISTRAR UNA VENTA')
    print(f'2.CONSULTAR UNA VENTA')
    print(f'3.SALIR\n')

    #OPCIÓN DEL USUARIO
    print(f'SELECCIONE EL NUMERO CORRESPONDINTE DE LA ACCIÓN A REALIZAR')
    op = input("OPCIÓN: ")

    if op == '1':
        articulos_List = []
        elementos_ActualesEnLista = contar_ElementosEnLaLista(ventas_List)
        folio = elementos_ActualesEnLista + 1
        print(f'\nPORFAVOR INGRESE LOS ARTICULOS QUE SE VENDIERON')
        desc_Articulo = input("DESCRIPCIÓN DEL ARTICULO: ")
        precio = float(input("PRECIO DEL ARTICULO: "))
        fecha_venta = datetime.date.today()
        datos_Articulo = datos_Articulo(desc_Articulo,precio,fecha_venta)
        articulos_List = articulos_List.append(datos_Articulo) 
        informacion_Venta = venta_Info()
        
        
