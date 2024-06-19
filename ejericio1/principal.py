import funciones as fn

trabajador=[]

while True:
    
    print('------------------------------------------------------')
    print('Bienvenidos al sistema de pago de sueldos.\n')
    print('1. Registrar trabajador.')
    print('2. Listar los trabajadores.')
    print('3. Imprimir planilla de sueldos.')
    print('4. Salir.')

    opc=int(input('Ingrese opcion: \n'))

    if opc == 1:
        fn.registrar_trabajador(trabajador)


    elif opc == 2:
        fn.lista_trabajadores(trabajador)


    elif opc == 3:
        fn.planilla_sueldos(trabajador)

    elif opc == 4:
        print('Hasta luego =)')
        break

    else:
        print("Ingrese opcion valida. Intente nuevamente.")     

              