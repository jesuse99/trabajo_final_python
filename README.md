# ExtremeBike – Simulador de Carrera de Ciclismo

ExtremeBike es un programa en Python que permite gestionar el registro de tiempos de ciclistas en una competencia. Calcula el tiempo promedio, identifica al ganador, compara con un tiempo récord e imprime el podio de los tres mejores participantes.

---

## Tecnologías utilizadas

- **Python 3.x**
- **Librerías externas**:
  - [`tabulate`](https://pypi.org/project/tabulate/): para mostrar tablas con formato.
  - [`rich`](https://pypi.org/project/rich/): para mensajes con colores, estilos y paneles atractivos.

---

## Funcionalidades

- Solicita el número de participantes y sus tiempos individuales.
- Calcula:
  - Tiempo total de cada ciclista en segundos.
  - Tiempo promedio de carrera.
  - Ganador con menor tiempo.
- Compara contra un tiempo récord ingresado manualmente.
- Muestra:
  - Tabla de todos los tiempos.
  - Tabla con ganador y promedio.
  - Mensaje si se batió el récord.
  - Podio con los tres mejores corredores.

## 2. Variables

- tiempo_ganador: Inicializado con infinito, se actualiza con el menor tiempo ingresado.
- numero_ganador: Guarda el número del participante con el mejor tiempo.
- tiempo_suma: Acumula la suma total de los tiempos para cálculo del promedio.
- tiempo_participantes, numeros_participantes, participantes: Listas para almacenar tiempos, números y diccionarios con datos de cada participante.

## 3. Validación de Entrada

Se utilizan funciones específicas para asegurar que los datos ingresados sean válidos antes de procesarlos:

### `validar_numero(mensaje)`
- Solicita al usuario un número entero.
- Verifica que sea mayor a 0.
- Reintenta en caso de error de tipo o valor negativo.

### `validar_hora(mensaje)`
- Similar a `validar_numero`, pero se usa para validar horas.
- Asegura que el valor ingresado sea un número entero y no negativo.

### `validar_tiempo(valor)`
- Asegura que el valor ingresado para **minutos o segundos** esté en el rango `[0–59]`.
- Devuelve `True` si el valor es inválido (para repetir la entrada).

## 4. Conversión de Tiempo

### `convertir_tiempo(tiempo_segundos)`
- Recibe una cantidad de segundos.
- Devuelve el tiempo convertido al formato estándar de **horas, minutos y segundos** (`hh:mm:ss`).
- Utiliza divisiones y restos para separar cada unidad.

## 5. Salida

- Usa tabulate para imprimir los resultados en forma de tablas.
- Imprime listado completo con números y tiempos formateados.
- Muestra ganador, tiempo ganador y tiempo promedio en formato hh:mm:ss.
- Imprime mensaje usando rich.Panel con colores y estilos según si se superó el récord o no.
- Muestra los 3 participantes con mejor tiempo en un podio. 

## Tareas por realizar

- [x] Crear funcion para validar tiempo (hh) (solo numeros)
- [x] Crear funcion para validar tiempo (mm y ss) (solo numeros)
- [x] Crear funcion para validar numero de participante (solo numeros)
- [x] Crear funcion para calcular y mostrar promedio
- [x] Crear lista y guardar los numeros de cada part
- [x] Crear lista y guardar los tiempos de cada part
- [x] Crear un menu de inicio

## Extras por realizar

- [x] Uso de librerias de pypy (por lo menos 3)
- [x] Documentacion del trabajo de como funciona en el repositorio
- [x] Presentacion del trabajo en (canva o gamma) 
- [x] Documentacion en el codigo (con comillas triples)
