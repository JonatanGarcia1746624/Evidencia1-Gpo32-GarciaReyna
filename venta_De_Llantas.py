from collections import namedtuple
import datetime
import time


articulo_list = []
venta_list = {}

Salida1 = int(0)
while Salida1 == int(0):
    venta_Info = namedtuple("Venta","Fecha_V,Desc_V,Cant_V,Precio_V")

    print(f'BASE DE DATOS "LLANTAS DON ELIAZAR"')
    print(f'1.REGISTRAR UNA VENTA')
    print(f'2.CONSULTAR UNA VENTA')
    print(f'3.SALIR')
    op = input("OPCIÓN:")
    print()

    if op == "1":
        Folio = int()
        print("DIGITE EL NUMERO DE FOLIO DE VENTA")
        print("SI DIGITA UN FOLIO NO EXISTENTE NO SE REGISTRARA")
        print("EL SISTEMA MARCARA ERROR Y VOLVERA AL MENU")
        num_Folio = int(input("FOLIO: "))
        print()

        if num_Folio in venta_list.keys():
            print("¡¡¡FOLIO YA EXISTENTE!!!\n")
        else:
            Folio = num_Folio
            Salida2 = int(0)
            while Salida2 == int(0):
                fecha_venta = str(datetime.date.today())
                desc_Articulo = str(input("DESCRIPCIÓN DEL ARTICULO: "))
                cantidad_Articulo = int(input("CANTIDAD: "))
                precio = float(input("PRECIO DEL ARTICULO: "))
                datos_Venta = venta_Info(fecha_venta, desc_Articulo,cantidad_Articulo,precio)
                articulo_list.append(datos_Venta)
                print(f'DESEA AGREGAR OTRO ARTICULO SI[0], NO[1]')
                exit = int(input("OPCIÓN: "))
                Salida2 = exit
            articulo_list2 = articulo_list.copy()
            venta_list[num_Folio] = articulo_list2
            del(articulo_list[:])
            print(f'\n***VENTA REGISTRADA CON EXITO***')
            print(f'\n{venta_list}\n')
            Salida1 = int(0)
            