CARGOS=['ceo','desarrollador','analista de datos']

def registrar_trabajador(trabajador):
    print('Registrar trabajador\n')
    nombre = input('Ingrese nombre del trabajador: ').lower()
    cargo = input('Ingrese cargo del trabajador (CEO/Desarrollador/Analista de datos): ').lower()
    while cargo not in CARGOS:
        print('El cargo ingresado es invalido, intente otra vez.')
        cargo = input('Ingrese cargo del trabajador (CEO/Desarrollador/Analista de datos): ').lower()
    sueldo_bruto = int(input('Ingrese sueldo bruto del trabajador: '))

    #calcular descuentos

    DescSalud = sueldo_bruto * 0.07
    DescAFP = sueldo_bruto * 0.12
    LiquidoPagar = sueldo_bruto - DescSalud - DescAFP

    trabajador.append({
        'Nombre' : nombre,
        'Cargo' : cargo,
        'SueldoBruto' : sueldo_bruto,
        'descSalud' : DescSalud,
        'descAFP' : DescAFP,
        'Liquido a pagar' : LiquidoPagar
    })

def lista_trabajadores(trabajador):
    for trabajadores in trabajador:
        print(trabajadores) 

def planilla_sueldos(trabajador):
    cargo_seleccionado = input('Ingrese cargo del trabajador para imprimir planilla sino presione ENTER para imprimir todos los trabajadores: ').lower()
    if cargo_seleccionado == '':
        trabajadores_a_imprimir = trabajador
        NombreArchivo = 'planilla_todos.txt'
    elif cargo_seleccionado in CARGOS:
        trabajadores_a_imprimir = []

        for trabajadores in trabajador['Cargo'] == cargo_seleccionado:
            trabajadores_a_imprimir.append(trabajador)    

        NombreArchivo = f'planilla_{cargo_seleccionado}.txt'
    else:
        print('cargo no valido')
        return

    with open (NombreArchivo, 'w') as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f'Nombre y Apellido: {trabajador['Nombre']}\n')
            archivo.write(f'Cargo: {trabajador['Cargo']}\n')       
            archivo.write(f'Sueldo Bruto: {trabajador['SueldoBruto']}\n')   
            archivo.write(f'Descuento de salud: {trabajador['descSalud']}\n')   
            archivo.write(f'Descuento AFP: {trabajador['descAFP']}\n')   
            archivo.write(f'Liquido a pagar del trabajador: {trabajador['Liquido a pagar']}\n\n')   

