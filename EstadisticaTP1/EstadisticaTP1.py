import random
import matplotlib.pyplot as plt
 
def cumples(k):
   return [random.randint(1, 365) for _ in range(k)]

# Esta función genera las fechas de cumpleaños para k personas.
# Recibe parametros k número de personas en el grupo.
# La función devuelve una lista de k fechas de cumpleaños (enteros entre 1 y 365).

def hay_coincidencia(cumples):
    return len(cumples) != len(set(cumples))

# Esta función verifica si hay al menos dos personas con el mismo cumpleaños en un grupo dado.
# Recibe parametro de la funcion cumples(list), lista de fechas de cumpleaños.
# La función devuelve un valor booleano, True si hay al menos una coincidencia, False en caso contrario.
# set(cumples) convierte la lista de fechas de cumpleaños cumples en un conjunto, lo que elimina las fechas de cumpleaños duplicadas.
# len(cumples) != len(set(cumples)) compara la longitud de la lista original cumples con la longitud del conjunto resultante. Si son diferentes, significa que había al menos dos personas con el mismo cumpleaños en el grupo.

def proporcion_coincidencia(k, N):
    coincidencias = sum(hay_coincidencia(cumples(k)) for _ in range(N))
    return coincidencias / N

# Esta función estima la probabilidad de que al menos dos personas en un grupo de k personas compartan el    mismo cumpleaños, utilizando N repeticiones.
# Recibe parametros k número de personas en el grupo y N número de repeticiones.
# sum(hay_coincidencia(cumples(k)) for _ in range(N)) genera N muestras de cumpleaños para un grupo de k personas y cuenta cuántas veces ocurre la coincidencia.
# El resultado se divide entre N para obtener la proporción de veces que ocurre la coincidencia.
# La función devuelve un valot float como una estimación de la probabilidad de coincidencia.

N = 1000
random.seed(7)
muestras = [proporcion_coincidencia(k, N) for k in range(1, 51)]
# repeticiones para cada valor de k
# Simulación para k entre 1 y 50 personas

for k, probabilidad in enumerate(muestras, 1):
    print(f"Para k={k}, la probabilidad estimada es: {probabilidad}")
# Los resultados se imprimen en forma de un bucle for, donde se muestra la probabilidad estimada para cada valor de k. Cada resultado está formateado con f-strings, mostrando el valor de k y la probabilidad estimada correspondiente.


plt.plot(range(1, 51), muestras, marker='o', linestyle='-')
plt.xlabel('Número de personas (k)')
plt.ylabel('Probabilidad estimada')
plt.title('Probabilidad de coincidencia de cumpleaños')
plt.grid(True)
plt.show()