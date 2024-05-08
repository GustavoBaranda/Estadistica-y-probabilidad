# Entrega del Trabajo de Simulación 2
""" 
    Grupo de trabajo nro. 7 
    
    Integrantes
    Maria Eugenia Bava
    Alejandro moises Abadi
    Catriel Escobar
    Hector Marcelo Galimberti
    Gisela Croci
    Gerardo Castellanos Torres
    Gustavo Daniel Baranda Cabrera
    
    ## Simulación (ejercicio a entregar)

    Armar una simulación basada en $N=100$ repeticiones que permita estimar el promedio de paquetes necesarios para conseguir llenar el álbum de figuritas del Mundial Qatar 2022. **[OPCIONAL]** Si es posible, representar el histograma de la cantidad de paquetes necesarios para completar el álbum a partir de la simulación. Puede usarse ``import seaborn as sns`` y ``sns.histplot()``.

    A diferencia de la resolución a mano, aquí propondremos una versión más realista: el álbum del Mundial Qatar 2022 tiene ``figus_total=860`` y vamos a suponer que el paquete no trae una figurita, sino varias: ``figus_paquete=5``. Además, Panini, empresa creadora del álbum del Mundial Qatar 2022, asegura que NO vienen figuritas repetidas por paquete. Para resolver este problema, podés optar por simularlo de acuerdo con esto que asegura Panini, o no. Es tu elección.


    **[PISTAS]** Para la construcción de la simulación, se sugiere la siguiente estructura, ya que no hemos estimado otra cosa que no sean probabilidades y, para este problema, necesitamos estimar una esperanza.

    1.  Para el armado del bullet "1. Experimento aleatorio", definir la función ``cuantos_paquetes(figus_total, figus_paquete)`` que dado el tamaño del álbum (``figus_total``) y la cantidad de figuritas por paquete (``figus_paquete``) genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.
    2.  Para el armado del bullet "2: Muestra aleatoria", definir una semilla, fijar ``N`` y armar ``N=100`` muestras de ``cuantos_paquetes(figus_total, figus_paquete)`` que se guarden en ``muestras``.
    3.  En esta instancia, como vimos, estaríamos armando el bullet "3: Una función _filtro_ que caracteriza el evento E" para luego estimar $P(E)$ por la frecuencia relativa de su aparición en las $N$ muestras. Sin embargo, aquí no hay evento para estimar: lo que queremos estimar es una esperanza. Para hacerlo, la aproximaremos por su promedio muestral, es decir, por el promedio de lo observado en ``muestras``. Para ello, podés usar el comando ``np.mean(muestras)``. Esto nos dará una estimación del promedio de paquetes necesarios para completar un álbum del Mundial Qatar 2022 a partir de una simulación de $N$ replicaciones.

    **[SUGERENCIA PARA EL BULLET 1]** Armar la función ``cuantos_paquetes(figus_total, figus_paquete)`` puede ser desafiante. Te compartimos una posible estructura que puede ayudarte a implementarla.

    - Implementá una función ``crear_album(figus_total)`` para crear un vector ``album`` que tenga un total de ``figus_total`` ceros. Es decir, vamos a representar al álbum por un vector en el que cada posición representa el estado de una figurita con dos valores: 0, para indicar que aún no la conseguimos, y 1, para indicar que sí. El álbum se inicia con todas sus posiciones en 0, hasta que empezamos a comprar figuritas y pegarlas.

    - Implementá una función ``comprar_paquete(figus_total,figus_paquete)`` que, dada la cantidad de figuritas por paquete (figus_paquete), genere un ``paquete`` (lista) de figuritas al azar. Si respetamos lo que afirma Panini de que no hay figuritas repetidas por paquete, usá el comando ``rd.sample``, ya que estaremos tomando una muestra de figuritas sin reposición.

    - Implementá la función ``pegar_figus(album,paquete)`` que complete con un 1 las figuritas del álbum que te hayan tocado. Recordá que los vectores se indexan desde 0, entonces, te va a convenir que la posición ``[i]`` del ``album`` toma el valor 1 si alguno de los elementos de la lista ``figus`` contiene al valor ``i``. Pero, para eso, generá las figuritan en ``range(0,figus_total)``, es decir, figuritas que toman valores de 0 hasta ``figus_total-1``. Lo importante es que aquellas figuritas que no te hayan tocado conserven el 0 en la posición correspondiente del vector ``album``. En este problema, no abordamos la complejidad que significaría intercambian y considerar todas las repetidas que podés tener.

    - Implementá la función ``album_incompleto(album)`` que recibe un vector ``album`` y devuelve ``True`` si el álbum ``A`` no está completo y ``False`` si lo está. Recordá que un álbum estará incompleto siempre que haya al menos un cero en alguna de sus posiciones.

    - Por último, utilizá todas estas funciones para crear una única función que las invoque y que se llame ``cuantos_paquetes(figus_total, figus_paquete)`` que cuente la cantidad de paquetes necesarios hasta completar el álbum. Necesitarás usar la estructura de control ``while()``, pues comprarás paquetes mientras el álbum siga incompleto; y deberás generar un contador de ``paquetes_comprados`` que arranque en 0 y sume un 1 cada vez que compres un nuevo paquete.
"""

# Estas líneas de código importan las bibliotecas necesarias para la simulación y la visualización de datos. 
import random 
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

# Definición de variables
# figus_total Esta variable representa el número total de figuritas en el álbum.
# figus_paquete Esta variable representa la cantidad de figuritas que contiene el paquete.
figus_total = 860
figus_paquete = 5


# La función crear_album(figus_total) recibe como parámetro figus_total, que indica el número total de figuritas en el álbum. 
# Esta función inicializa y devuelve un álbum vacío representado con una lista. 
# Cada posición en la lista corresponde a una figurita en el álbum, y un valor de 0 indica que esa figurita no se ha sido conseguida. 
# Este álbum se utiliza como punto de partida para el proceso de llenado del álbum durante la simulación.
def crear_album(figus_total):
    album = []
    for _ in range(figus_total):
        album.append(0)
    return album
 

# La función devuelve un paquete de figuritas generado aleatoriamente en una lista. 
# Esta lista contendrá elementos únicos que representan las figuritas incluidas en el paquete. 
# Garantizamos que los elementos sean únicos con el uso de random.sample(), que evita la repetición de figuritas en el paquete.
def comprar_paquete(figus_total, figus_paquete):
    return random.sample(range(figus_total), figus_paquete)
    

# La función pegar_figus(album, paquete) recibe como parámetro (album) que genera la funcion crear_album() 
# donde se van a pegar las figuritas y el parámetro (paquete) que contiene las figuritas que se van a pegar en el álbum.
# La función recorre cada figurita en el paquete utilizando un bucle for. Para cada figurita en el paquete, 
# actualiza la posición correspondiente en el # album cambiando el valor de 0 a 1.
def pegar_figus(album, paquete):
    for figuritas in paquete:
        album[figuritas] = 1
        

# La función album_imcompleto(album) recibe un parámetro album, que es una lista que representa el álbum de figuritas 
# y determina si hay figuritas por conseguir en el álbum representado por la lista. 
# Retorna True si hay al menos una figurita no conseguida (valor 0) en el álbum, y False si todas las figuritas han sido conseguidas (valor 1).
def album_imcompleto(album):
    for figuritas in album:
        if figuritas == 0:
            return True
    return False 


# La función cuantos_paquetes(figus_total, figus_paquete) la funcion recibe los parametros figus_total que indica el número total de figuritas 
# en el álbum y el parametro figus_paquete que representa la cantidad de figuritas en cada paquete
# La funcion cuantos_paquetes(figus_total, figus_paquete) simula el proceso de llenado del álbum, comprando paquetes de figuritas hasta que el 
# álbum esté completo, y retorna el número total de paquetes comprados durante la simulación.
def cuantos_paquetes(figus_total, figus_paquete):   
    album = crear_album(figus_total)
    paquetes_comprados = 0 
    while (album_imcompleto(album)):
        paquete = comprar_paquete(figus_total, figus_paquete)
        pegar_figus(album, paquete)
        paquetes_comprados += 1
    
    return paquetes_comprados 
    

# random.seed(7): Establece la semilla del generador de números aleatorios en 7, lo que garantiza resultados reproducibles.
# N = 100: Define el número de repeticiones del experimento.    
# Crea una lista llamada muestras que contiene los resultados de la función cuantos_paquetes(figus_total, figus_paquete) 100 veces. 
# Cada elemento de la lista representa la cantidad de paquetes necesarios para completar el álbum en una repetición del experimento.
random.seed(7) 
N = 100

muestras = [cuantos_paquetes(figus_total, figus_paquete) for _ in range(N)]


# Se calcula el promedio de los valores en la lista muestras, que representa la cantidad de paquetes necesarios para completar 
# el álbum en cada repetición del experimento y es almacenada calculado el promedio en la variable promedio_muestral, 
# que representa el promedio de paquetes necesarios para completar el álbum, basado en las 100 repeticiones del experimento,
# para ello se utiliza numpy.mean(muestras) que calcula el promedio de los valores en la lista muestras. 
promedio_muestral = numpy.mean(muestras)
print(f"Promedio muestral de paquetes necesarios: {promedio_muestral}")


# El código genera un histograma que muestra la distribución de la cantidad de paquetes necesarios para completar el álbum, 
# basado en 100 repeticiones del experimento"
plt.figure(figsize=(10, 6))
sns.histplot(muestras, bins=25, kde=True, color='green')
plt.xlabel('Cantidad de paquetes necesarios')
plt.ylabel('Ocurrencias')
plt.title('Muestras de paquetes necesarios para completar el álbum')
plt.axvline(promedio_muestral, color='red', linestyle='dashed', linewidth=2,
label=f'Promedio muestral : {promedio_muestral}')
plt.legend()
plt.show()