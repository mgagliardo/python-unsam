def palabra_a_geringoso(palabra):
  vocales = ['a', 'e', 'i', 'o', 'u']
  for vocal in vocales:
      reemplazo = vocal + 'p' + vocal
      palabra = palabra.replace(vocal, reemplazo)
  return palabra

def diccionario_geringoso(lista_palabras):
  lista_palabras_geringoso = []
  for palabra in lista_palabras:
      lista_palabras_geringoso.append(palabra_a_geringoso(palabra))
  return lista_palabras_geringoso

lista_palabras = [ 'banana', 'manzana', 'mandarina' ]

lista_palabras_geringoso = diccionario_geringoso(lista_palabras)
print(lista_palabras_geringoso)
# ['bapanapanapa', 'mapanzapanapa', 'mapandaparipinapa']
