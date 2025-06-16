from tabulate import tabulate
from rich import print
from rich.panel import Panel

# Declaración e inicialización de variables
tiempo_ganador = float('inf') 
numero_ganador = 0
tiempo_suma = 0
tiempo_participantes = []
numeros_participantes = []
participantes = []

        
def validar_numero(mensaje):
    """
    Función que se usa para solicitar un numero entero.
    Realiza una validacion para asegurar que el usuario
    ingrese únicamente un número postivo. Vuelve a solicitar 
    el dato si se introduce texto u otro carácter.
    """
    valor_valido = False
    while not valor_valido:
        valor = input(mensaje)
        if valor.isnumeric():
            valor = int(valor)
            if valor <= 0:
                print("\nError: Valor no válido. Por favor, ingresa solo números enteros positivos.")
            else:
                valor_valido = True
        else:
            print("\nError: Valor no válido. Por favor, ingresa solo números enteros positivos.")
    return valor
    
def validar_hora(mensaje):
    """
    Funcion que se usa para solicitar un numero entero.
    Realiza una validacion para asegurarse de que el usuario
    ingrese unicamente un numero y no un string, dentro del rango
    de tiempo correcto, de lo contrario vuelve a solicitar el dato 
    si se introduce texto u otro caracter.
    """
    valor_valido = False
    while not valor_valido:
        valor = input(mensaje)
        if valor.isnumeric():
            valor = int(valor)
            if (valor < 0 or valor > 23):
                print("\nError: Valor no válido. Por favor, ingresa un tiempo valido.")
            else:
                valor_valido = True
        else:
            print("\nError: Valor no válido. Por favor, ingresa un tiempo valido.")
    return valor

def validar_minsec(mensaje):
    """
    Función que recibe un valor, puede ser tanto minutos
    como segundos, realiza una comprobacion del valor
    ingresado y si se encuentra en el rango correcto,
    retorna el valor 
    """
    valor_valido = False
    while not valor_valido:
        valor = input(mensaje)
        if valor.isnumeric():
            valor = int(valor)
            if (valor < 0 or valor > 59):
                print("\nError: Valor no válido. Por favor, ingresa un tiempo valido.")
            else:
                valor_valido = True
        else:
            print("\nError: Valor no válido. Por favor, ingresa un tiempo valido.")
    return valor

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

print("Bienvenvido a ExtremeBike, el programa perfecto para carreras de ciclismo \n")
parts = validar_numero("Ingrese cantidad participantes: ")
print(parts)

for part in range(parts):
    numero = validar_numero("Ingrese numero de participante: ")
    numeros_participantes.append(numero)
    
    horas = validar_hora("Ingrese horas del participante: ")
    minutos = validar_minsec("Ingrese minutos del participante: ")
    segundos = validar_minsec("Ingrese segundos del participante: ")

    tiempo = (horas * 3600) + (minutos * 60) + segundos 
    tiempo_participantes.append(tiempo)
    participantes.append({
        "numero": numero,
        "tiempo_segundos": tiempo,
        "tiempo_formateado": f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    })

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

h_ganador, m_ganador, s_ganador = convertir_tiempo(tiempo_ganador)

tiempo_promedio_segundos = tiempo_suma / parts
h_promedio, m_promedio, s_promedio = convertir_tiempo(int(tiempo_promedio_segundos))

tabla = [
    ["Número ganador", numero_ganador],
    ["Tiempo ganador", f"{h_ganador:02d}:{m_ganador:02d}:{s_ganador:02d}"],
    ["Tiempo promedio", f"{h_promedio:02d}:{m_promedio:02d}:{s_promedio:02d}"]
]

print(tabulate(tabla, headers=["Descripción", "Resultado"], tablefmt="fancy_grid"))

print("--- Ingrese tiempo record --")

horas = validar_hora("Ingrese horas del participante: ")
minutos = validar_minsec("Ingrese minutos del participante: ")
segundos = validar_minsec("Ingrese segundos del participante: ")

record = (horas * 3600) + (minutos * 60) + segundos 

if tiempo_ganador < record:
    mensaje = "🎉 ¡Nuevo tiempo récord! El ganador batió el récord 🏆"
    print(Panel.fit(f"[bold green]{mensaje}[/bold green]", border_style="bright_green"))
else:
    mensaje = "⏱️ No se superó el tiempo récord. Intenta de nuevo 💪"
    print(Panel.fit(f"[bold yellow]{mensaje}[/bold yellow]", border_style="red"))

participantes_ordenados = sorted(participantes, key=lambda x: x['tiempo_segundos'])

podio = []
puestos = ["🥇 1er Puesto", "🥈 2do Puesto", "🥉 3er Puesto"]

for i in range(min(3, len(participantes_ordenados))):
    p = participantes_ordenados[i]
    podio.append([puestos[i], p["numero"], p["tiempo_formateado"]])

print("\n[bold cyan]--- Podio de los 3 primeros participantes ---[/bold cyan]")
print(tabulate(podio, headers=["Puesto", "Número", "Tiempo"], tablefmt="fancy_grid"))