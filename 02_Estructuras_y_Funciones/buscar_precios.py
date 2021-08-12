def buscar_precio(fruta):
    with open('../Data/precios.csv', "rt") as file:
        for line in file:
            nombre_fruta, precio = line.split(',')
            if fruta in nombre_fruta:
                print("El precio de un cajon de {0} es: {1}".format(fruta, precio))
                return
    print("{} no figura en el listado de precios.".format(fruta))

buscar_precio('Frambuesa')
# Output: El precio de un cajon de Frambuesa es: 34.35

buscar_precio('Kale')
# Output: Kale no figura en el listado de precios.
