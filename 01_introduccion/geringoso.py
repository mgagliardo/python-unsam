# Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' 
# según corresponda luego de cada vocal.

cadena = 'Geringoso'

for vocal in ['a', 'e', 'i', 'o', 'u']:
  reemplazo = vocal + 'p' + vocal
  cadena = cadena.replace(vocal, reemplazo)

print(cadena)
