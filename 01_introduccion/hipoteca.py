mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
pago_mensual = 2684.11
saldo = 500000.0
tasa = 0.05
total_pagado = 0.0

while saldo > 0:
    mes = mes + 1
    pago = pago_mensual
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        pago = pago + pago_extra
    if saldo < pago:
        pago = saldo
        saldo = saldo - pago
    else:
        saldo = saldo * ( 1 + tasa / 12 ) - pago
    total_pagado = total_pagado + pago
    print("{0} {1} {2}".format(mes, round(total_pagado, 2), round(saldo, 2)))

print("Total pagado: {}".format(round(total_pagado, 2)))
print("Meses: {}".format(mes))
