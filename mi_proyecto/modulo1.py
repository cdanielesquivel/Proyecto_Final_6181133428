import csv

def ingresar_ventas(ventas):
    while True:
        try:
            curso = input('Íngrese el nombre del curso: ')
            cantidad = int(input("Ingrese la cantidad de cursos: "))
            fecha = input('Ingrese la fecha de de laventa (AAAA-MM-DD): ')
            precio = float(input('Ingrese el precio del curso: '))
            cliente = input('Ingrese el nombre del cliente: ')
        except ValueError:
            print('Entradas no valida, por favor intentelo nuevamente!')
            continue
        
        venta = {
            'Curso': curso,
            'Cantidad': cantidad,
            'Precio': precio,
            'Fecha':fecha,
            'Cliente': cliente
        }
        ventas.append(venta)
        
        continuar = input('Desea ingresar otra venta s/n: ').lower()
        if continuar == 's':
            print("\n ------------  Ingresando otra Venta  ---------")
        elif continuar == 'n':
            break
        else:
            print('Opción no valida. Saliendo de ventas.')
            break
        

def guardar_ventas(ventas):
    if not ventas:
        print('No hay nada que guardar')
    else:
        try:
            with open('ventas.csv','w',newline='') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['Curso','Cantidad','Precio','Fecha','Cliente'])
                guardar.writeheader()
                guardar.writerows(ventas)
            print('Datos gardados exitosamente!')
        except Exception as e:
            print(f'Error al guarda el archivo {e}')