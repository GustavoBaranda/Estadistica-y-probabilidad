import random
import matplotlib.pyplot as plt
 
def cumples(k):
    return [random.randint(1, 365) for _ in range(k)]

N = 1000
random.seed(7)

""" 
def generar_muestras(N, k):
    muestras = []
    for _ in range(N):
        muestras.append(cumples(k))
    return muestras 
"""

def generar_muestras(N, k):
    return [cumples(k) for _ in range(N)]

def hay_coincidencia(cumples):
    return len(cumples) != len(set(cumples))

def proporcion_coincidencia(k, N):
    muestras = generar_muestras(N, k)
    coincidencias = sum(hay_coincidencia(muestra) for muestra in muestras)
    return coincidencias / N

probabilidades = [proporcion_coincidencia(k, N) for k in range(1, 51)]

for k, probabilidad in enumerate(probabilidades, 1):
    print(f"Para k={k}, la probabilidad estimada es: {probabilidad}")

plt.plot(range(1, 51), probabilidades, marker='o', linestyle='-')
plt.xlabel('Número de personas (k)')
plt.ylabel('Probabilidad estimada')
plt.title('Probabilidad de coincidencia de cumpleaños')
plt.grid(True)
plt.show()
