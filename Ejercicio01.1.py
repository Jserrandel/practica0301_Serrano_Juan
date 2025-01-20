#Escribir dos funciones, una función que reciba un número entero 
#positivo n y calcule el número de fibonacci asociado a ese número 
#de manera recursiva y otra función que haga la misma operación pero con bucles.
#Con ambas funciones, calcular y comparar el tiempo de ejecución para 
#n = (1, 10, 20, 30 y 40) por fuerza bruta.
import time
def fibonacci_recursivo(n):

    '''recibe un número entero 
positivo n y calcule el número de fibonacci asociado a ese número 
de manera recursiva'''

    if n <= 1:  
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_iterativo(n):

    '''reciba un número entero 
positivo n y calcule el número de fibonacci asociado con bucles'''

    if n <= 1:  
        return n
    a, b = 0, 1 
    for _ in range(2, n + 1):
        a, b = b, a + b 
    return b

n = int(input("Introduce el valor de n (entero positivo): "))

if n < 0: 
    print("Por favor, introduce un número entero positivo.")
else:
    inicio = time.time()  
    resultado_recursivo = fibonacci_recursivo(n)
    fin = time.time()  
    tiempo_recursivo = fin - inicio  

    inicio = time.time()
    resultado_iterativo = fibonacci_iterativo(n)
    fin = time.time()
    tiempo_iterativo = fin - inicio

    print(f"\nResultados para n = {n}:")
    print(f"Fibonacci (recursivo): {resultado_recursivo}, Tiempo: {tiempo_recursivo:.6f} segundos")
    print(f"Fibonacci (iterativo): {resultado_iterativo}, Tiempo: {tiempo_iterativo:.6f} segundos")