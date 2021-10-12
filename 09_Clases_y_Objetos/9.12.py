class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

class TorreDeControl(Cola):
    def nuevo_arribo(self, vuelo):
        self.encolar((vuelo, 'arribo'))
    
    def nueva_partida(self, vuelo):
        self.encolar((vuelo, 'partida'))

    def pista_vacia(self):
        return self.esta_vacia()

    def ver_estado(self):
        if not self.pista_vacia():
            aterrizajes = [vuelo[0] for vuelo in self.items if vuelo[1] == 'arribo']
            if aterrizajes:
                print("Vuelos esperando para aterrizar: {}.".format(', '.join(aterrizajes)))
            partidas = [vuelo[0] for vuelo in self.items if vuelo[1] == 'partida']
            if partidas:
                print("Vuelos esperando para despegar: {}.".format(', '.join(partidas)))
        else:
            print("No hay vuelos en espera.")

    def asignar_pista(self):
        vuelo = self.desencolar()
        cod_vuelo = vuelo[0]
        despegue_o_aterrizaje = 'aterrizó' if vuelo[1] == 'arribo' else 'despegó'
        print("El vuelo {} {} con éxito.".format(cod_vuelo, despegue_o_aterrizaje))
