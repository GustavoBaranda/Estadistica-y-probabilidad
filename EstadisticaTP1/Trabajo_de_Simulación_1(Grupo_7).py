# Entrega del Trabajo de Simulación 1
""" 
    Grupo de trabajo nro. 7 
    
    Integrantes
    Maria Eugenia Bava
    Alejandro moises Abadi
    Catriel Escobar
    Hector Marcelo Galimberti 
    Gustavo Daniel Baranda Cabrera

    Armar una simulación basada en $N=1000$ repeticiones que permita estimar la probabilidad de que al menos dos personas en un grupo de $k$ personas elegidas al azar cumpla años el mismo día. Dar una lista de las probabilidades estimadas en función de $k$ para $k$ entre 1 y 50. **[OPCIONAL]** Si es posible, representar esas probabilidades estimadas en un gráfico.

    Para la construcción de la simulación, se sugiere seguir la estructura propuesta en el apartado de simulaciones numéricas de este Notebook. Es decir, para un valor de $k$ que hayamos fijado, puede hacerse lo siguiente.

    1.  Para el armado del bullet "1. Experimento aleatorio", definir la función ``cumples(k)``, que devuelva ``k`` fechas de cumpleaños (``k`` números entre 1 y 365).
    2.  Para el armado del bullet "2: Muestra aleatoria", definir una semilla, fijar ``N`` y armar ``N=1000`` muestras de ``cumples(k)`` que se guarden en ``muestras``.
    3.  Para el armado del bullet "3: Una función _filtro_ que caracteriza el evento E", definir la función ``hay_coincidencia(cumples)`` que devuelva ``TRUE`` (o un 1) si hay una coincidencia en una lista ``cumples`` que sea pasada como argumento. Esta es la función que quizás sea más difícil de implementar. Hay muchas formas de hacerlo. Como pista, la función ``set()`` que ya usamos es una estructura de datos ideal para contener objetos sin repeticiones.
    4.  Para el armado del bullet "4: Aproximamos P(E) por la proporción de elementos de E en la muestra" contar la proporción de ``hay_coincidencia()`` en las ``N`` repeticiones de la muestra y devolver ese valor.

    **[SUGERENCIA]** Como quiere estimarse la probabilidad en las simulaciones para grupos de $k$ personas, donde $k$ varía desde 0 hasta 50 personas, puede crearse una función ``proporcion_coincidencia(k,N)`` que devuelva directamente una aproximación a la probabilidad de coincidencia en función del número de personas ``k``; sin tener que simular las ``N`` repeticiones en cada caso por separado. En esta función ``proporcion_coincidencia(k,N)`` pueden usarse, dentro, las funciones ``cumples()`` y ``hay_coincidencia()``.
"""

import random
import matplotlib.pyplot as plt
 
def cumples(k):
    return [random.randint(1, 365) for _ in range(k)]

# Esta función genera las fechas de cumpleaños para k personas.
# Recibe parametros k número de personas en el grupo.
# La función devuelve una lista de k fechas de cumpleaños (enteros entre 1 y 365).

random.seed(7)
N = 1000

# Se establece la semilla aleatoria usando random.seed(7). Esto asegura que los resultados sean reproducibles.
# N = 1000 indica el número de veces que se repetirá el experimento para estimar la probabilidad.

def generar_muestras(N, k):
    return [cumples(k) for _ in range(N)]

#La función genera N muestras de cumpleaños, donde cada muestra contiene k cumpleaños generados aleatoriamente utilizando la función cumples(k).

def hay_coincidencia(cumples):
    return len(cumples) != len(set(cumples))

# La función verifica si hay al menos dos personas en la lista cumples que comparten el mismo cumpleaños. 
# Esto se hace comparando la longitud de la lista cumples con la longitud del conjunto (que elimina duplicados).
# Si las longitudes son diferentes, significa que hay al menos una coincidencia de cumpleaños.

def proporcion_coincidencia(k, N):
    muestras = generar_muestras(N, k)
    coincidencias = sum(hay_coincidencia(muestra) for muestra in muestras)
    return coincidencias / N

# La función calcula la proporción de veces que ocurre la coincidencia de cumpleaños (al menos dos personas comparten cumpleaños) en un grupo de k personas, utilizando N repeticiones de muestras generadas aleatoriamente.
# Primero, genera N muestras de k cumpleaños cada una utilizando generar_muestras(N, k).
# Luego, verifica cuántas veces hay coincidencias en estas muestras utilizando la función hay_coincidencia(cumples).
# Finalmente, devuelve la proporción de muestras donde ocurrió al menos una coincidencia.
 
probabilidades = [proporcion_coincidencia(k, N) for k in range(1, 51)]
# Se crea una lista probabilidades que almacenará las probabilidades estimadas para cada número de personas k (desde 1 hasta 50).
# Para cada valor de k en el rango de 1 a 50, se llama a la función proporcion_coincidencia(k, N) para estimar la probabilidad y se almacena en la lista probabilidades.

for k, probabilidad in enumerate(probabilidades, 1):
    print(f"Para k={k}, la probabilidad estimada es: {probabilidad}")
# Se imprime en consola la probabilidad estimada de coincidencia para cada valor de k del 1 al 50.    

plt.plot(range(1, 51), probabilidades, marker='o', linestyle='-')
plt.xlabel('Número de personas (k)')
plt.ylabel('Probabilidad estimada')
plt.title('Probabilidad de coincidencia de cumpleaños')
plt.grid(True)
plt.show()
# Se utiliza matplotlib.pyplot para graficar las probabilidades estimadas en función del número de personas k.
# Se traza un gráfico donde el eje x representa k (número de personas) y el eje y representa la probabilidad estimada de coincidencia.
# Se añaden etiquetas a los ejes (plt.xlabel, plt.ylabel) y un título al gráfico (plt.title) para mayor claridad.
# Se muestra el gráfico utilizando plt.show().
