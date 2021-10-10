from datetime import datetime


def calcular_segundos(fecha_nacimiento):
    '''Recibe una fecha de nacimiento con formato 'dd/mm/yyyy' y retorna
       la cantidad de segundos del delta entre hoy y esa misma fecha.
    
    Pre: Un string con formato fecha 'dd/mm/yyyy'
    Pos: El delta entre hoy y esa misma fecha medido en segundos.
    '''
    format_str = '%d/%m/%Y'
    try:
        datetime_obj = datetime.strptime(fecha_nacimiento, format_str)
        fecha_hoy = datetime.today()
        if datetime_obj > fecha_hoy:
            raise ValueError("La fecha ingresada no puede ser posterior al dia de hoy.")
        else:
            return (fecha_hoy - datetime_obj).total_seconds()
    except ValueError as e:
        print(f"La fecha ingresada no es correcta o no condice con la propuesta: {e}")

if __name__ == '__main__':
    fecha_nacimiento = '07/08/1981'
    segundos_vividos = calcular_segundos(fecha_nacimiento)
    # print(f"La cantidad de segundos vividos es de {segundos_vividos}")
