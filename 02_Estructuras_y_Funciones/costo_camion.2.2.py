costo_total = 0.0
f = open('../data/Data/camion.csv', 'rt')
next(f)

for line in f:
    _, cajones, precio = line.split(',')
    costo_total = costo_total + int(cajones) * float(precio.rstrip())

print("Costo total: {}".format(costo_total))
