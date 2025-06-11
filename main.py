from tabulate import tabulate

# Declaración e inicialización de variables
TIEMPO_RECORD = 55
tiempo_ganador = float('inf') 
numero_ganador = 0
tiempo_suma = 0
tiempo_participantes = []
numeros_participantes = []

def validar_tiempo(valor):
    """
    Función que recibe un valor, puede ser tanto minutos
    como segundos, valida si se encuentra en el rango
    correcto y devuelve el resultado de la validación
    """
    tiempo_valido = True
    if (valor < 0 or valor > 59):
        print("El valor no es valido, vuelva a intentarlo")
        tiempo_valido = False
    return not tiempo_valido

def convertir_tiempo(tiempo_segundos):
    """
    Función que permite recibe el tiempo en segundos, y
    realiza la conversion y devuelve el tiempo en horas, 
    minutos y segundos
    """
    horas = tiempo_segundos // 3600
    resto = tiempo_segundos % 3600
    minutos = resto // 60
    segundos = resto % 60
    return horas, minutos, segundos
        
def validar_hora(mensaje):
    """
    Funcion que se usa para solicitar un numero entero.
    Usa un bloque try-except para asegurarse de que el usuario
    ingrese unicamente un numero y no un string, de lo contrario 
    vuelve a solicitar el dato si se introduce texto u otro caracter.
    """
    try:
        # Intenta convertir la entrada del usuario a un entero.
        valor = int(input(mensaje))
        # Chequea que el entero sea positivo
        # Si tiene éxito, devuelve el valor y sale del bucle.
        if valor < 0:
            print("\nError: Las horas no pueden ser negativas. Ingresar solo numeros enteros positivos.")
            return validar_hora(mensaje)
        else:
            return valor
    except ValueError:
        # Si la conversión falla, le informa al usuario y el bucle continúa.
        print("\nError: Valor no valido. Por favor, ingresa solo numeros enteros positivos. ")
        return validar_hora(mensaje)
        
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


print("Bienvenvido a ExtremeBike, el programa perfecto para carrera de ciclismo \n")
parts = validar_numero("Ingrese cantidad participantes: ")
for part in range(parts):
    numero = validar_numero("Ingrese numero de participante: ")
    numeros_participantes.append(numero)
    
    horas = validar_hora("Ingrese horas del participante: ")

    minutos = int(input("Ingrese minutos del participante: "))
    while validar_tiempo(minutos):
        minutos = int(input("Ingrese minutos del participante: "))
    
    segundos = int(input("Ingrese segundos del participante: "))
    while validar_tiempo(segundos):
        segundos = int(input("Ingrese segundos del participante: "))

    tiempo = (horas * 3600) + (minutos * 60) + segundos 
    tiempo_participantes.append(tiempo)

    tiempo_suma = tiempo_suma + tiempo
    
    # Se agrega el tiempo del participante como el ganador si es menor que el mejor tiempo anterior
    if tiempo < tiempo_ganador:
        tiempo_ganador = tiempo
        numero_ganador = numero

tabla_participantes = []
for i in range(parts):
    h, m, s = convertir_tiempo(tiempo_participantes[i])
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


print("--- Ingrese tiempo record --")

horas = validar_hora("Ingrese horas del participante: ")

minutos = int(input("Ingrese minutos: "))
while validar_tiempo(minutos):
    minutos = int(input("Ingrese minutos: "))

segundos = int(input("Ingrese segundos: "))
while validar_tiempo(segundos):
    segundos = int(input("Ingrese segundos: "))

record = (horas * 3600) + (minutos * 60) + segundos 

if record < TIEMPO_RECORD:
    print("Nuevo tiempo record! el ganador batio el record")
