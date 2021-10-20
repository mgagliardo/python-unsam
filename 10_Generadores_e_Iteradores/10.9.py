import csv
from vigilante import vigilar

lines = vigilar('../Data/mercadolog.csv')
rows = csv.reader(lines)
for row in rows:
    print(row)

# ['Esparrago', ' 632.69', ' 228']
# ['Ajo', ' 878.39', ' 98']
# ['Acelga', ' 22.67', ' 1035']
