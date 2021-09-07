import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x, y

def caen_en_circulo_unitario():
    x, y = generar_punto()
    return x ** 2 + y ** 2 < 1


N = 100000
G = sum([caen_en_circulo_unitario() for _ in range(N)])
print(f'Aproximacion de pi: {G/N*4}')

# Escribí un programa estimar_pi.py que genere cien mil puntos aleatorios con la función generar_punto()
# calcule la proporción de estos puntos que caen en el círculo unitario (usando ¿x^2 + y^2 < 1?)
# y use este resultado para dar una aproximación de pi.
