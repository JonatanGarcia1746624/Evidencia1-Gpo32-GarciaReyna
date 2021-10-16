from collections import namedtuple
import datetime
import time


articulo_list = []
venta_list = {}

Salida1 = int(0)
while Salida1 == int(0):
    venta_Info = namedtuple("Venta","Fecha_V,Desc_V,Cant_V,Precio_V")

    print(f'\nBASE DE DATOS "LLANTAS DON ELIAZAR"')
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
                print("AGREGAR ARTICULO")
                fecha_venta = str(datetime.date.today())
                desc_Articulo = str(input("DESCRIPCIÓN DEL ARTICULO: "))
                cantidad_Articulo = float(input("CANTIDAD: "))
                precio = float(input("PRECIO DEL ARTICULO: "))
                datos_Venta = venta_Info(fecha_venta, desc_Articulo,cantidad_Articulo,precio)
                articulo_list.append(datos_Venta)
                print(f'\nDESEA AGREGAR OTRO ARTICULO SI[0], NO[1]')
                exit = int(input("OPCIÓN: "))
                Salida2 = exit
                print()
            articulo_list2 = articulo_list.copy()
            venta_list[num_Folio] = articulo_list2
            del(articulo_list[:])
            print(f'\n***VENTA REGISTRADA CON EXITO***\n')
            pos = venta_list[num_Folio]
            print(f'FECHA DE VENTA: {fecha_venta}')
            subtotal = int(0)
            for elemento in pos:
                importe = elemento.Cant_V * elemento.Precio_V
                print(f'DESCRIPCIÓN ARTICULO: {elemento.Desc_V}')
                print(f'CANTIDAD: {elemento.Cant_V}')
                print(f'PRECIO UNITARIO: {elemento.Precio_V}')
                print(f'IMPORTE: {importe}')
                subtotal += importe
                print()
            print(f'SUBTOTAL: {subtotal}')
            print(f'IVA(16%): {subtotal * 0.16}')
            print(f'TOTAL: {(subtotal) + (subtotal * 0.16)}')
            Salida1 = int(0)
    else:
        if op == "2":
            print(f'\nCONSULTAR UNA VENTA')
            print(f'INGRESE EL FOLIO DE LA VENTA QUE DESEA CONSULTAR')
            num_Venta = int(input("Numero de Folio: "))
            if num_Venta in venta_list.keys():
                pos = venta_list[num_Venta]
                print("\n***FOLIO ENCONTRADO***\n")
                print(f'FECHA: {pos[0].Fecha_V}')
                subtotal = int(0)
                for elemento in pos:
                    importe = elemento.Cant_V * elemento.Precio_V
                    print(f'DESCRIPCIÓN ARTICULO: {elemento.Desc_V}')
                    print(f'CANTIDAD: {elemento.Cant_V}')
                    print(f'PRECIO UNITARIO: {elemento.Precio_V}')
                    print(f'IMPORTE: {importe}')
                    subtotal += importe
                    print()
                print(f'SUBTOTAL: {subtotal}')
                print(f'IVA(16%): {subtotal * 0.16}')
                print(f'TOTAL: {(subtotal) + (subtotal * 0.16)}')
            else:
                print("\n¡¡¡FOLIO NO ENCONTRADO!!!")
        else:
            if op == "3":
                Salida1 = int(1)
        