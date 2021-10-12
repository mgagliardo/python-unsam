class Canguro:
    def __init__(self, nombre, lista=[]):
        self.nombre = nombre
        self.contenido_marsupio = lista
    
    def __repr__(self):
        return f'Canguro({self.nombre})'

    def __str__(self):
        return "Nombre: {}.\nContenido del marsupio:\n\t{}.".format(self.nombre, '\n\t'.join([object.__str__(obj) for obj in self.contenido_marsupio]))

    def meter_en_marsupio(self, obj):
        self.contenido_marsupio.append(obj)

if __name__ == '__main__':
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)
    print(madre_canguro)


# canguro_malo.py corregido

# """Este código continene un 
# bug importante y dificil de ver
# """
 
# class Canguro:
#     """Un Canguro es un marsupial."""
 
#     def __init__(self, nombre, contenido=[]):
#         """Inicializar los contenidos del marsupio.
 
#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         self.nombre = nombre
#         self.contenido_marsupio = contenido

"""
    repr() devuelve la representacion "oficial" de un objeto
    Mientras que str() es la representacion de un objeto.  objeto Canguro
    Canguro no encuentra una representacion de la misma (con la llamada __repr__)
    Por tanto lo unico faltante es una representacion de dicho objeto con su nombre
    dado que ya estamos imprimiendo el contenido de la lista en el metodo especial __str__
"""

#    def __repr__(self):
#        return f'Canguro({self.nombre})'

#    def __str__(self):
#        """devuelve una representación como cadena de este Canguro.
#        """
#        t = [ self.nombre + ' tiene en su marsupio:' ]
#        for obj in self.contenido_marsupio:
#            s = '    ' + object.__str__(obj)
#            t.append(s)
#        return '\n'.join(t)
 
#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.
# 
#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)

# #%%
# madre_canguro = Canguro('Madre')
# cangurito = Canguro('gurito')
# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)
# 
# print(madre_canguro)
# 
# # Al ejecutar este código todo parece funcionar correctamente.
# # Para ver el problema, imprimí el contenido de cangurito.
