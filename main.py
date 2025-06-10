TIEMPO_RECORD = 1
tiempo_ganador = 0
numero_ganador = 0
tiempo_suma = 0
tiempo_parts = []

def validar_tiempo(valor):
    tiempo_valido = False
    if (valor < 0 or valor > 59):
        print("El valor no es valido, vuelva a intentarlo")
        tiempo_valido = False
    else:
        print("Excelente, pasemos a la siguiente")
        tiempo_valido = True
    return not tiempo_valido

def convertir_tiempo(tiempo_segundos):
    horas, minutos, segundos = 0,0,0
    while tiempo_segundos > 0:
        if tiempo_segundos >= 3600:
            tiempo_segundos = tiempo_segundos % 3600
            horas += 1
        if tiempo_segundos >= 60:
            tiempo_segundos = tiempo_segundos % 60
            minutos += 1
        else:
            segundos = tiempo_segundos
            tiempo_segundos = 0
    return horas, minutos, segundos
        

def validar_numero(mensaje):
    """
    Función que se usa para solicitar un numero entero.
    Usa un bucle y un bloque try-except para asegurar que el usuario
    ingrese únicamente un número. Vuelve a solicitar el dato si se
    introduce texto u otro carácter.
    """
    while True:
        try:
            # Intenta convertir la entrada del usuario a un entero.
            valor = int(input(mensaje))
            # Si tiene éxito, devuelve el valor y sale del bucle.
            return valor
        except ValueError:
            # Si la conversión falla, le informa al usuario y el bucle continúa.
            print("\nError: Valor no válido. Por favor, ingresa solo números enteros.")


parts = validar_numero("Ingrese cantidad participantes: ")
for part in range(parts):
    numero = validar_numero("Ingrese numero de participante: ")
    
    
    # funcion para validar horas (completar)
    horas = 1

    minutos = int(input("Ingrese minutos del participante: "))
    while validar_tiempo(minutos):
        minutos = int(input("Ingrese minutos del participante: "))
    
    segundos = int(input("Ingrese segundos del participante: "))
    while validar_tiempo(segundos):
        segundos = int(input("Ingrese segundos del participante: "))

    tiempo = (horas * 3600) + (minutos * 60) + segundos 
    print(tiempo)
    tiempo_parts.append(tiempo)

    tiempo_suma = tiempo_suma + tiempo
    if tiempo > tiempo_ganador:
        tiempo_ganador = tiempo
        numero_ganador = numero

if parts > 0:
    horas, minutos, segundos = convertir_tiempo(tiempo_ganador)
    print("El numero ganador de la carrera:", numero_ganador, "y tiempo que empleo:", f"{horas}:{minutos}:{segundos}")
    
    # completar funcion calcular y mostrar promedio
    tiempo_promedio = 0
    print("Tiempo promedio entre ciclistas:", tiempo_promedio)

# completar funcion calcular si batio record
record = input("Ingrese tiempo record (hh/mm/ss): ")
record = 1
if record < TIEMPO_RECORD:
    print("Nuevo tiempo record! el ganador batio el record")