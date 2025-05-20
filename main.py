from datetime import time
from time import strftime, gmtime

TIME_RECORD = time(4, 42, 15)
time_win = time(23, 59, 59)
num_win = 0
suma = 0

part = int(input("Ingrese cantidad participantes: "))
for i in range(part):
    numero = int(input("Ingrese numero de participante: "))
    
    tiempo = input("Ingrese tiempo de participante (hh/mm/ss): ")
    tiempo = time(int(tiempo[0:2]), int(tiempo[3:5]), int(tiempo[6:8]))
    
    suma += tiempo.second
    if tiempo < time_win:
        time_win = tiempo
        num_win = numero

if part > 0:
    print("El numero ganador de la carrera:", num_win, "y tiempo que empleo:", time_win)
    
    time_average = strftime("%H:%M:%S", gmtime(suma/part))
    print("Tiempo promedio entre ciclistas:", time_average)

record = input("Ingrese tiempo record (hh/mm/ss): ")
record = time(int(record[0:2]), int(record[3:5]), int(record[6:8]))
if record < TIME_RECORD:
    print("Nuevo tiempo record! el ganador batio el record")