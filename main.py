from tabulate import tabulate
TIEMPO_RECORD = 1
tiempo_ganador = float('inf') 
numero_ganador = 0
tiempo_suma = 0
tiempo_parts = []
numeros_participantes = []

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
    horas = tiempo_segundos // 3600
    resto = tiempo_segundos % 3600
    minutos = resto // 60
    segundos = resto % 60
    return horas, minutos, segundos
        

def validar_numero(mensaje):
    """
    Función que se usa para solicitar un numero entero.
    Usa un bloque try-except para asegurar que el usuario
    ingrese únicamente un número. Vuelve a solicitar el dato si se
    introduce texto u otro carácter.
    """
    try:
        # Intenta convertir la entrada del usuario a un entero.
        valor = int(input(mensaje))
        # Chequea que el entero sea positivo
        # Si tiene éxito, devuelve el valor y sale del bucle.
        if valor < 1:
            print("\nError: Valor no válido. Por favor, ingresa solo números enteros positivos.")
            return validar_numero(mensaje)
        else:
            return valor
    except ValueError:
        # Si la conversión falla, le informa al usuario y el bucle continúa.
        print("\nError: Valor no válido. Por favor, ingresa solo números enteros positivos.")
        return validar_numero(mensaje)


parts = validar_numero("Ingrese cantidad participantes: ")
for part in range(parts):
    numero = validar_numero("Ingrese numero de participante: ")
    numeros_participantes.append(numero)
    
    # funcion para validar horas (completar)
    horas = 1

    minutos = int(input("Ingrese minutos del participante: "))
    while validar_tiempo(minutos):
        minutos = int(input("Ingrese minutos del participante: "))
    
    segundos = int(input("Ingrese segundos del participante: "))
    while validar_tiempo(segundos):
        segundos = int(input("Ingrese segundos del participante: "))

    tiempo = (horas * 3600) + (minutos * 60) + segundos 
    tiempo_parts.append(tiempo)

    tiempo_suma = tiempo_suma + tiempo
    
    # Se agrega el tiempo del participante como el ganador si es menor que el mejor tiempo anterior
    if tiempo < tiempo_ganador:
        tiempo_ganador = tiempo
        numero_ganador = numero

tabla_participantes = []
for i in range(parts):
    h, m, s = convertir_tiempo(tiempo_parts[i])
    tabla_participantes.append([numeros_participantes[i], f"{h:02d}:{m:02d}:{s:02d}"])

print("\nListado de participantes y tiempos:")
print(tabulate(tabla_participantes, headers=["Número Participante", "Tiempo (hh:mm:ss)"], tablefmt="fancy_grid"))


if parts > 0:
    horas, minutos, segundos = convertir_tiempo(tiempo_ganador)
    # completar funcion calcular y mostrar promedio
    tiempo_promedio = 1

    tabla = [
        ["Número ganador", numero_ganador],
        ["Tiempo ganador", f"{horas:02d}:{minutos:02d}:{segundos:02d}"],
        ["Tiempo promedio", tiempo_promedio]
    ]
    
    print(tabulate(tabla, headers=["Descripción", "Resultado"], tablefmt="fancy_grid"))

# completar funcion calcular si batio record
record = input("Ingrese tiempo record (hh/mm/ss): ")
record = 1
if record < TIEMPO_RECORD:
    print("Nuevo tiempo record! el ganador batio el record")