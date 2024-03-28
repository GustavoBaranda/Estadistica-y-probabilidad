import random

def cumples(k):
    """Genera k fechas de cumpleaños al azar."""
    return [random.randint(1, 365) for _ in range(k)]

def hay_coincidencia(cumples):
    """Verifica si hay al menos dos personas con el mismo cumpleaños."""
    return len(cumples) != len(set(cumples))

def proporcion_coincidencia(k, N):
    """Estima la probabilidad de coincidencia para un grupo de k personas."""
    coincidencias = sum(hay_coincidencia(cumples(k)) for _ in range(N))
    return coincidencias / N

# Simulación para k entre 1 y 50 personas
N = 1000
resultados = [proporcion_coincidencia(k, N) for k in range(1, 51)]

# Imprimir resultados
for k, probabilidad in enumerate(resultados, 1):
    print(f"Para k={k}, la probabilidad estimada es: {probabilidad}")




