# Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' 
# según corresponda luego de cada vocal.

cadena = 'Geringoso'
vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
  reemplazo = vocal + 'p' + vocal
  cadena = cadena.replace(vocal, reemplazo)

print(cadena)
