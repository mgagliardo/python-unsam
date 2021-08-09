saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra = 1000
mes = 0

while saldo > 0:
    saldo = saldo * ( 1 + tasa / 12 ) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    if mes < 12:
      saldo = saldo - pago_extra
      total_pagado = total_pagado + pago_extra
    mes = mes + 1
    print("Total pagado al mes {0}: {1}".format(mes, round(total_pagado, 2)))


print('Total pagado', round(total_pagado, 2))
