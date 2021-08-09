import math

radio = float(input("Ingrese por teclado el radio r de una esfera: "))
volumen = 4/3 * math.pi * (radio ** 3)

print("El volumen de una esfera de radio {0} es {1}".format(radio, volumen))
