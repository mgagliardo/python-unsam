def tablas_multiplicar():
  # Calculo la cantidad de tablas
  # En base a los parametros que se pasen
  tablas = tuple(range(0, 10))
  
  # Formateo segun el range que se pide
  # La primer y ultima string son solo por cuestiones meramente
  # De prolijidad y no hacen al ejercicio en si
  str_print = "%7d " + "%3d " * (len(tablas) - 2) + "%3d"
  
  print(str_print % tablas)
  print("---------------------------------------------")

  # NDA: No encontre la manera de hacerlo *solo* con sumas
  # Asi que lo hice con multiplicaciones
  for tabla in tablas:
    tabla_final = ()
    for elem in tablas:
        tabla_final += (tabla * elem,)
    # Otra vez, solo por cuestion de formato
    format_str = "%d: " % tabla + "%4d " + "%3d " * (len(tablas) - 1)
    print(format_str % tabla_final)

tablas_multiplicar()

#       0   1   2   3   4   5   6   7   8   9
#---------------------------------------------
# 0:    0   0   0   0   0   0   0   0   0   0
# 1:    0   1   2   3   4   5   6   7   8   9
# 2:    0   2   4   6   8  10  12  14  16  18
# 3:    0   3   6   9  12  15  18  21  24  27
# 4:    0   4   8  12  16  20  24  28  32  36
# 5:    0   5  10  15  20  25  30  35  40  45
# 6:    0   6  12  18  24  30  36  42  48  54
# 7:    0   7  14  21  28  35  42  49  56  63
# 8:    0   8  16  24  32  40  48  56  64  72
# 9:    0   9  18  27  36  45  54  63  72  81
