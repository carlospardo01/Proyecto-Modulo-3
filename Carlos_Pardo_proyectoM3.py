#Importamos las librerías para numeros aleatorios y para graficar
import numpy as np
import random
import matplotlib.pyplot as plt
#Se crea una función para simular el recorrido de las canicas en la Máquina de Galton
def simular_canicas(no_canicas, niveles_obstaculos):
    """
    Simula la caída de un número específico de canicas en una máquina de Galton con un número específico de niveles.
    - no_canicas: Número total de canicas a simular.
    - niveles_obstaculo: Número de niveles de obstáculos que atraviesa cada canica.
    """
    #Lista para almacenar los resultados de la posición de cada Canica
    resultados = []
    #Buscar la posición de cada Canica
    for i in range(no_canicas):
        #La posición inicial de cada Canica es 0 por lo que inician desde el centro
        posicion = 0
        #Se revisa si la posición de la Canica es +1 o -1
        for i in range(niveles_obstaculos):
            #Se revisa a qué lado se puede mover, izquierda (-1) o derecha (+1)
            Direccion = random.choice([-1, 1])
            #Se actualiza la posición según el movimiento aleatorio sumando la posición y la dirección
            posicion += Direccion
        #Se guarda el resultado de la posición en una lista
        resultados.append(posicion)
    #Se devuelve la lista con los datos obtenidos
    return resultados
# Función para graficar los resultados en un histograma
def graficar_histograma(resultados):
    """
    Genera un histograma con la distribución final de las canicas.
    - resultados: Lista con las posiciones de las canicas.
    """
    #Se crea el histograma, se le indica que no debe superar las 13 barras o contenedores, se le indica que el color de la línea de la gráfica y el color de las barras
    plt.hist(resultados, bins=13, edgecolor='blue',color='skyblue')
    #Se indica el nombre del eje X
    plt.xlabel("Contenedores")
    #Se indica el nombre del eje Y
    plt.ylabel("Número de canicas")
    #Se coloca el título a la gráfica
    plt.title("Simulación de la Máquina de Galton")
    #Se muestra la gráfica
    plt.show()
#Se indica la cantidad de canicas a simular, el ejercicio decía que 3000
no_canicas = 3000
#Se indica la cantidad de niveles de obstáculos en la máquina, el ejercicio decía 12
niveles_obstaculos = 12
#Se hace la simulación llamando la función simular_canicas
resultados_simulacion = simular_canicas(no_canicas, niveles_obstaculos)
#Se genera el histograma con los resultados de la simulación
graficar_histograma(resultados_simulacion)