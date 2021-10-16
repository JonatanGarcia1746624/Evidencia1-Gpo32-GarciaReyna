#MODULOS QUE SE UTILIZARAN
from collections import namedtuple
import datetime
import time

#FUNCIONES A UTILIZAR
#1.CONTAR ELEMENTOS EN LA LISTA
def contar_ElementosEnLaLista(lista):
    numElementos = len(lista)
    return numElementos


#LISTA DE LAS VENTAS
ventas_List = {}

#SWITCH PARA SALIR DEL WHILE
Salida1 = int(0)
salida2 = int(0)
while Salida1 == int(0):
    #FORMATO DE LA LISTA DE VENTAS
    venta_Info = namedtuple("VENTA","infoVenta")

    #REGISTRO DE ARTICULOS VENDIOS
    datos_Articulo = namedtuple("ARTICULO","DescArticulo,Precio,fecha_venta")
    #MENU
    print(f'LLANTAS EL "TÍO JUAN"')
    print(f'1.REGISTRAR UNA VENTA')
    print(f'2.CONSULTAR UNA VENTA')
    print(f'3.SALIR\n')

    #OPCIÓN DEL USUARIO
    print(f'SELECCIONE EL NUMERO CORRESPONDINTE DE LA ACCIÓN A REALIZAR')
    op = input("OPCIÓN: ")

    if op == '1':
        folios_ActualesEnLista = contar_ElementosEnLaLista(ventas_List)
        folio = folios_ActualesEnLista + 1
        articulos_List = ()
        while salida2 == int(0):
            print(f'\nPORFAVOR INGRESE EL ARTICULO VENDIDO')
            desc_Articulo = str(input("DESCRIPCIÓN DEL ARTICULO: "))
            precio = float(input("PRECIO DEL ARTICULO: "))
            fecha_venta = str(datetime.date.today())
            informacion_Articulos = datos_Articulo(desc_Articulo.upper(),precio,fecha_venta)
            articulos_List.append(informacion_Articulos)
            informacion_Venta = articulos_List
            check_Salida = int(input("DESEA AGREGAR OTRO ARTICULO SI[0], NO[1]: "))
            salida2 = check_Salida
        ventas_List[folio] = informacion_Venta
        print(f'\n"***VENTA REGISTRADA CON EXITO***"')
        print(f'\n{ventas_List}\n')
    Salida1 = int(0)
