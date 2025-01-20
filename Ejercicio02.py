#Escribir una función que lea dos ficheros csv con una lista larga de datos de
#personas (50 personas y 1000 personas) y llame a dos funciones que pongan
#su nombre en formato capitalizado y calculen la letra de DNI correspondiente.
#Realiza la comprobación de rendimiento con la librería cProfile y muestra los
#datos. Describe que indica cada dato que nos proporciona cProfile.

import csv
import time
import cProfile

def capitalizar_nombre(nombre):
    return nombre.strip().title()

def calcular_letra_dni(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[dni % 23]

def procesar_csv(fichero):
    resultados = []
    with open(fichero, "r") as archivo:
        lector = csv.reader(archivo)
        next(lector)  
        for fila in lector:
            nombre = capitalizar_nombre(fila[0])
            dni = int(fila[1])
            letra_dni = calcular_letra_dni(dni)
            resultados.append((nombre, dni, letra_dni))
    return resultados


def medir_rendimiento():
    ficheros = ["50.csv", "1000.csv"]  
    for fichero in ficheros:
        print(f"Procesando fichero: {fichero}")
        resultados = procesar_csv(fichero)
        print(f"Se procesaron {len(resultados)} registros del fichero {fichero}.")


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    medir_rendimiento()
    profiler.disable()


    profiler.print_stats(sort="cumulative")
